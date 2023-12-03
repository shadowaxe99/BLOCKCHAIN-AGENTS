```python
import hashlib
import os
from cryptography.fernet import Fernet

# Constants for environment variable names
ENV_SECRET_KEY = 'AI_AGENTS_SECRET_KEY'

# Exception classes for security-related issues
class SecurityError(Exception):
    """Base class for security-related exceptions."""
    pass

class EncryptionKeyError(SecurityError):
    """Raised when there is an issue with the encryption key."""
    pass

# Helper functions for security operations
def generate_key():
    """
    Generates a new key for encryption and decryption.
    """
    return Fernet.generate_key()

def load_encryption_key():
    """
    Loads the encryption key from an environment variable.
    Raises EncryptionKeyError if the key is not found or invalid.
    """
    key = os.getenv(ENV_SECRET_KEY)
    if not key:
        raise EncryptionKeyError("Encryption key not found in environment variables.")
    try:
        # Ensure the key is in a valid format
        Fernet(key)
    except ValueError as e:
        raise EncryptionKeyError("Invalid encryption key format.") from e
    return key

def encrypt_data(data):
    """
    Encrypts data using the loaded encryption key.
    """
    key = load_encryption_key()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data):
    """
    Decrypts data using the loaded encryption key.
    """
    key = load_encryption_key()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data

def hash_data(data):
    """
    Hashes data using SHA-256.
    """
    sha_signature = hashlib.sha256(data.encode()).hexdigest()
    return sha_signature

# Security class for AI agents
class AgentSecurity:
    """
    Security class for handling encryption, decryption, and hashing of AI agent data.
    """

    def __init__(self):
        self.encryption_key = load_encryption_key()

    def secure_agent_data(self, data):
        """
        Encrypts and hashes AI agent data for secure storage.
        """
        encrypted_data = encrypt_data(data)
        data_hash = hash_data(data)
        return encrypted_data, data_hash

    def verify_agent_data(self, data, data_hash):
        """
        Verifies that the provided data matches the hash.
        """
        return hash_data(data) == data_hash

    def retrieve_secure_data(self, encrypted_data):
        """
        Decrypts AI agent data for use in the application.
        """
        return decrypt_data(encrypted_data)

# Example usage
if __name__ == "__main__":
    # Set up a new agent security instance
    agent_security = AgentSecurity()

    # Example data to secure
    example_data = "Sensitive information about AI agent."

    # Secure the data
    encrypted_data, data_hash = agent_security.secure_agent_data(example_data)

    # Verify the data
    if agent_security.verify_agent_data(example_data, data_hash):
        print("Data verification successful.")

    # Retrieve the data
    decrypted_data = agent_security.retrieve_secure_data(encrypted_data)
    print(f"Decrypted data: {decrypted_data}")
```