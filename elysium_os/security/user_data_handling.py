```python
import json
from cryptography.fernet import Fernet
from elysium_os.security.access_control import authenticateUser

# Load the key from a file or environment variable for encryption/decryption
# It's important to keep this key secure and not expose it in the code
with open('encryption_key.txt', 'rb') as file:
    encryption_key = file.read()

fernet = Fernet(encryption_key)

def encrypt_user_data(user_data):
    """
    Encrypts user data using Fernet symmetric encryption.
    
    :param user_data: A dictionary containing user data.
    :return: An encrypted byte string of the user data.
    """
    # Convert the user data to a JSON string and then to bytes
    user_data_bytes = json.dumps(user_data).encode('utf-8')
    # Encrypt the user data
    encrypted_data = fernet.encrypt(user_data_bytes)
    return encrypted_data

def decrypt_user_data(encrypted_data, user_id):
    """
    Decrypts user data using Fernet symmetric encryption.
    
    :param encrypted_data: An encrypted byte string of the user data.
    :param user_id: The ID of the user whose data is being decrypted.
    :return: A dictionary containing the decrypted user data.
    """
    # Authenticate the user before decrypting their data
    if not authenticateUser(user_id):
        raise PermissionError("User authentication failed.")
    
    # Decrypt the user data
    decrypted_data_bytes = fernet.decrypt(encrypted_data)
    # Convert the bytes back to a JSON string and then to a dictionary
    decrypted_data = json.loads(decrypted_data_bytes.decode('utf-8'))
    return decrypted_data

def store_user_data(user_data, user_id):
    """
    Stores user data securely by encrypting it before saving to disk.
    
    :param user_data: A dictionary containing user data.
    :param user_id: The ID of the user whose data is being stored.
    """
    encrypted_data = encrypt_user_data(user_data)
    # Store the encrypted data in a file named after the user ID
    with open(f'user_data_{user_id}.enc', 'wb') as file:
        file.write(encrypted_data)

def retrieve_user_data(user_id):
    """
    Retrieves and decrypts user data from storage.
    
    :param user_id: The ID of the user whose data is being retrieved.
    :return: A dictionary containing the decrypted user data.
    """
    try:
        # Read the encrypted data from a file named after the user ID
        with open(f'user_data_{user_id}.enc', 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = decrypt_user_data(encrypted_data, user_id)
        return decrypted_data
    except FileNotFoundError:
        raise FileNotFoundError("User data file not found.")
    except Exception as e:
        raise Exception(f"An error occurred while retrieving user data: {e}")
```