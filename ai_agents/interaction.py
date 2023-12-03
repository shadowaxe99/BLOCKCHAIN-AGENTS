```python
# ai_agents/interaction.py

class InteractionManager:
    def __init__(self):
        # Initialize interaction manager with necessary data structures
        self.active_interactions = {}

    def initiate_interaction(self, agent_id, user_id, interaction_type, interaction_data):
        """
        Begin an interaction between an AI agent and a user.
        :param agent_id: Unique identifier for the AI agent.
        :param user_id: Unique identifier for the user.
        :param interaction_type: Type of interaction (e.g., conversation, task assistance).
        :param interaction_data: Data relevant to the interaction.
        :return: Interaction ID for tracking the interaction.
        """
        interaction_id = self._generate_interaction_id(agent_id, user_id)
        self.active_interactions[interaction_id] = {
            'agent_id': agent_id,
            'user_id': user_id,
            'interaction_type': interaction_type,
            'interaction_data': interaction_data,
            'status': 'active'
        }
        return interaction_id

    def process_interaction(self, interaction_id, new_data):
        """
        Process ongoing interaction with new data.
        :param interaction_id: Interaction ID for the ongoing interaction.
        :param new_data: New data to be processed in the interaction.
        """
        if interaction_id in self.active_interactions:
            interaction = self.active_interactions[interaction_id]
            # Process the new data based on the type of interaction
            # This is a placeholder for the actual processing logic
            interaction['interaction_data'].update(new_data)
        else:
            raise ValueError(f"No active interaction found for ID: {interaction_id}")

    def end_interaction(self, interaction_id):
        """
        End an interaction.
        :param interaction_id: Interaction ID for the interaction to be ended.
        """
        if interaction_id in self.active_interactions:
            self.active_interactions[interaction_id]['status'] = 'ended'
        else:
            raise ValueError(f"No active interaction found for ID: {interaction_id}")

    def _generate_interaction_id(self, agent_id, user_id):
        """
        Generate a unique interaction ID based on agent and user IDs.
        :param agent_id: Unique identifier for the AI agent.
        :param user_id: Unique identifier for the user.
        :return: A unique interaction ID.
        """
        return f"{agent_id}_{user_id}_{len(self.active_interactions) + 1}"

    def get_interaction_status(self, interaction_id):
        """
        Get the status of an interaction.
        :param interaction_id: Interaction ID for the interaction in question.
        :return: Status of the interaction.
        """
        if interaction_id in self.active_interactions:
            return self.active_interactions[interaction_id]['status']
        else:
            raise ValueError(f"No active interaction found for ID: {interaction_id}")

# Example usage:
# interaction_manager = InteractionManager()
# interaction_id = interaction_manager.initiate_interaction('agent123', 'user456', 'conversation', {'message': 'Hello, how can I assist you today?'})
# interaction_manager.process_interaction(interaction_id, {'message': 'I need help with my account.'})
# status = interaction_manager.get_interaction_status(interaction_id)
# interaction_manager.end_interaction(interaction_id)
```