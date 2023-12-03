```python
import hashlib
import os
from elysium_os.security.user_data_handling import UserData

class AccessControl:
    def __init__(self):
        # This dictionary will hold the user credentials, with USER_ID as key and password hash as value
        self.user_credentials = {}

    def hash_password(self, password):
        """Create a hash of the password for secure storage."""
        salt = os.urandom(32)  # A new salt for this user
        pwdhash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return salt + pwdhash

    def register_user(self, user_id, password):
        """Register a new user with a hashed password."""
        if user_id in self.user_credentials:
            raise ValueError("User ID already exists")
        self.user_credentials[user_id] = self.hash_password(password)

    def authenticate_user(self, user_id, password):
        """Authenticate a user by comparing the provided password with the stored hash."""
        if user_id not in self.user_credentials:
            return False
        stored_password = self.user_credentials[user_id]
        salt = stored_password[:32]  # 32 is the length of the salt
        stored_hash = stored_password[32:]
        pwdhash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return pwdhash == stored_hash

    def change_user_password(self, user_id, old_password, new_password):
        """Allow a user to change their password."""
        if not self.authenticate_user(user_id, old_password):
            raise PermissionError("Authentication failed")
        self.user_credentials[user_id] = self.hash_password(new_password)

    def remove_user(self, user_id):
        """Remove a user from the system."""
        if user_id in self.user_credentials:
            del self.user_credentials[user_id]
        else:
            raise KeyError("User ID does not exist")

# Example usage:
# access_control = AccessControl()
# access_control.register_user(USER_ID, 'my_secure_password')
# is_authenticated = access_control.authenticate_user(USER_ID, 'my_secure_password')
# access_control.change_user_password(USER_ID, 'my_secure_password', 'my_new_secure_password')
# access_control.remove_user(USER_ID)
```

This code provides a basic access control system with functions to register users, authenticate them, change passwords, and remove users. It uses the `hashlib` library to securely hash passwords with a salt. The `os` library is used to generate a random salt. The `UserData` import is a placeholder for a module that would handle user-related data operations, which is assumed to be part of the shared dependencies.