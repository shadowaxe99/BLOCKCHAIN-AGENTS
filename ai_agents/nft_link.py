```python
import uuid
from elysium_os.blockchain.nft_transactions import transfer_ownership, remove_nft
from elysium_os.blockchain.blockchain_integration import BlockchainInterface

class NFTLink:
    def __init__(self, blockchain_interface: BlockchainInterface):
        self.blockchain_interface = blockchain_interface

    def link_agent_to_nft(self, agent_id: str, owner_id: str) -> str:
        """
        Links an AI agent to a unique NFT and registers it on the blockchain.

        :param agent_id: The unique identifier of the AI agent.
        :param owner_id: The unique identifier of the owner.
        :return: The unique identifier of the linked NFT.
        """
        nft_id = str(uuid.uuid4())
        nft_data = {
            'agent_id': agent_id,
            'owner_id': owner_id,
            'nft_id': nft_id
        }
        self.blockchain_interface.register_nft(nft_data)
        return nft_id

    def transfer_nft(self, nft_id: str, new_owner_id: str) -> bool:
        """
        Transfers the ownership of an NFT to a new owner.

        :param nft_id: The unique identifier of the NFT.
        :param new_owner_id: The unique identifier of the new owner.
        :return: True if the transfer was successful, False otherwise.
        """
        return transfer_ownership(nft_id, new_owner_id)

    def unlink_agent_from_nft(self, nft_id: str) -> bool:
        """
        Unlinks an AI agent from its NFT and removes the NFT from the blockchain.

        :param nft_id: The unique identifier of the NFT to be removed.
        :return: True if the removal was successful, False otherwise.
        """
        return remove_nft(nft_id)

# Example usage:
# blockchain_interface = BlockchainInterface()
# nft_linker = NFTLink(blockchain_interface)
# agent_nft_id = nft_linker.link_agent_to_nft(agent_id='agent-123', owner_id='user-456')
# transfer_successful = nft_linker.transfer_nft(nft_id=agent_nft_id, new_owner_id='user-789')
# unlink_successful = nft_linker.unlink_agent_from_nft(nft_id=agent_nft_id)
```