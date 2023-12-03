```python
import json
from web3 import Web3
from web3.contract import Contract

# Assuming the existence of a smart contract for handling NFT transactions
from .blockchain_integration import NFT_CONTRACT_ABI, NFT_CONTRACT_ADDRESS

class NFTTransactions:
    def __init__(self, provider_url: str):
        self.web3 = Web3(Web3.HTTPProvider(provider_url))
        self.contract = self.web3.eth.contract(
            address=NFT_CONTRACT_ADDRESS,
            abi=NFT_CONTRACT_ABI
        )

    def transfer_ownership(self, from_address: str, to_address: str, token_id: int, private_key: str) -> dict:
        """
        Transfer the ownership of an NFT from one address to another.

        :param from_address: The current owner's address.
        :param to_address: The new owner's address.
        :param token_id: The unique identifier for the NFT.
        :param private_key: The private key of the current owner for signing the transaction.
        :return: Transaction receipt.
        """
        nonce = self.web3.eth.getTransactionCount(from_address)
        txn_dict = self.contract.functions.transferFrom(
            from_address,
            to_address,
            token_id
        ).buildTransaction({
            'chainId': 1,  # Assuming Ethereum mainnet; change as needed
            'gas': 2000000,
            'gasPrice': self.web3.toWei('50', 'gwei'),
            'nonce': nonce,
        })

        signed_txn = self.web3.eth.account.signTransaction(txn_dict, private_key=private_key)
        txn_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        receipt = self.web3.eth.waitForTransactionReceipt(txn_hash)
        return receipt

    def remove_agent_from_world(self, token_id: int) -> bool:
        """
        Remove an AI agent from the 3D world upon NFT sale.

        :param token_id: The unique identifier for the NFT linked to the AI agent.
        :return: True if the removal was successful, False otherwise.
        """
        # Placeholder for the actual logic to remove the agent from the world
        # This would involve interaction with the 3D world system and the AI agent's data
        try:
            # Assuming a function exists to handle the removal of an agent
            # from the 3D world based on the NFT token ID
            success = self.handle_agent_removal(token_id)
            return success
        except Exception as e:
            print(f"Error removing agent from world: {e}")
            return False

    def handle_agent_removal(self, token_id: int) -> bool:
        """
        Handle the removal of an AI agent from the 3D world.

        :param token_id: The unique identifier for the NFT linked to the AI agent.
        :return: True if the removal was successful, False otherwise.
        """
        # Actual implementation would depend on the 3D world system's API
        # For now, we return True to indicate a successful placeholder operation
        return True

# Example usage:
# nft_transactions = NFTTransactions(provider_url='https://mainnet.infura.io/v3/YOUR_INFURA_API_KEY')
# receipt = nft_transactions.transfer_ownership(
#     from_address='0xFromAddress',
#     to_address='0xToAddress',
#     token_id=123,
#     private_key='0xPrivateKey'
# )
# print(f"Transaction receipt: {json.dumps(receipt, indent=4)}")
# success = nft_transactions.remove_agent_from_world(token_id=123)
# print(f"Agent removed: {success}")
```