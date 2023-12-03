```python
from .data_protection import handleDataProtection
from .user_data_handling import encryptUserData, decryptUserData
from .access_control import authenticateUser

__all__ = [
    'handleDataProtection',
    'encryptUserData',
    'decryptUserData',
    'authenticateUser'
]
```