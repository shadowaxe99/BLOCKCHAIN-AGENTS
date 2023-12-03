```python
import uuid
from elysium_os.security.user_data_handling import encryptUserData, decryptUserData
from elysium_os.security.access_control import authenticateUser
from elysium_os.feedback.user_feedback import collectUserFeedback

class User:
    def __init__(self, username, password, email):
        self.user_id = str(uuid.uuid4())
        self.username = username
        self.password = encryptUserData(password)
        self.email = email
        self.owned_nfts = []
        self.owned_agents = []
        self.feedback = []

    def authenticate(self, password):
        return authenticateUser(self.username, password)

    def add_owned_nft(self, nft_id):
        if nft_id not in self.owned_nfts:
            self.owned_nfts.append(nft_id)

    def remove_owned_nft(self, nft_id):
        if nft_id in self.owned_nfts:
            self.owned_nfts.remove(nft_id)

    def add_owned_agent(self, agent_id):
        if agent_id not in self.owned_agents:
            self.owned_agents.append(agent_id)

    def remove_owned_agent(self, agent_id):
        if agent_id in self.owned_agents:
            self.owned_agents.remove(agent_id)

    def submit_feedback(self, feedback):
        self.feedback.append(collectUserFeedback(feedback))

    def get_user_data(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'owned_nfts': self.owned_nfts,
            'owned_agents': self.owned_agents
        }

    def update_password(self, old_password, new_password):
        if self.authenticate(old_password):
            self.password = encryptUserData(new_password)
            return True
        return False

    def __str__(self):
        return f"User({self.username}, {self.email})"

# Example usage:
# user = User('john_doe', 's3cur3p@ssw0rd', 'john.doe@example.com')
# user.authenticate('s3cur3p@ssw0rd')
# user.add_owned_nft('nft-1234')
# user_data = user.get_user_data()
# print(user)
```