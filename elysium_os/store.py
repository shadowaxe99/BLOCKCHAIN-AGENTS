```python
import uuid
from elysium_os.personas.persona import Persona
from elysium_os.blockchain.nft_transactions import NFTData, transferNFTOwnership
from elysium_os.security.data_protection import encryptUserData, decryptUserData

class Store:
    def __init__(self):
        self.available_agents = {}
        self.agent_nft_mapping = {}

    def list_agents(self):
        """List all available AI agents in the store."""
        return self.available_agents

    def purchase_agent(self, user_id, agent_id):
        """
        Purchase an AI agent and link it to a unique NFT.
        
        Args:
            user_id (str): The ID of the user purchasing the agent.
            agent_id (str): The ID of the agent being purchased.
        
        Returns:
            str: NFT ID linked to the purchased AI agent.
        """
        if agent_id not in self.available_agents:
            raise ValueError("Agent ID not found in store.")
        
        # Simulate the purchase transaction and NFT creation
        nft_id = str(uuid.uuid4())
        nft_data = NFTData(nft_id=nft_id, owner_id=user_id, asset_id=agent_id)
        self.agent_nft_mapping[agent_id] = nft_id
        
        # Transfer NFT ownership to the user
        transferNFTOwnership(nft_data)
        
        # Encrypt user data for security
        encrypted_user_data = encryptUserData(user_id)
        
        return nft_id

    def add_agent_to_store(self, agent_data):
        """
        Add a new AI agent to the store.
        
        Args:
            agent_data (dict): Data representing the AI agent to be added.
        """
        agent_id = str(uuid.uuid4())
        self.available_agents[agent_id] = agent_data

    def remove_agent_from_store(self, agent_id):
        """
        Remove an AI agent from the store.
        
        Args:
            agent_id (str): The ID of the agent to be removed.
        """
        if agent_id in self.available_agents:
            del self.available_agents[agent_id]
        else:
            raise ValueError("Agent ID not found in store.")

    def get_agent_nft(self, agent_id):
        """
        Retrieve the NFT ID linked to an AI agent.
        
        Args:
            agent_id (str): The ID of the agent.
        
        Returns:
            str: NFT ID linked to the AI agent.
        """
        return self.agent_nft_mapping.get(agent_id, None)

# Example usage:
# store = Store()
# store.add_agent_to_store({'name': 'Elysium Helper', 'description': 'Assists with tasks in the 3D world.'})
# user_id = 'user-123'
# agent_id = list(store.list_agents().keys())[0]
# nft_id = store.purchase_agent(user_id, agent_id)
# print(f"Agent purchased with NFT ID: {nft_id}")
```