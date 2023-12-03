class AgentCustomizationError(Exception):
    """Custom exception for agent customization errors."""
    pass


class AgentCustomizer:
    def __init__(self, agent_data):
        """
        Initialize the AgentCustomizer with the agent's data.

        :param agent_data: A dictionary containing the agent's attributes and states.
        """
        self.agent_data = agent_data

    def update_attribute(self, attribute_name, new_value):
        """
        Update the value of a specific attribute for the agent.

        :param attribute_name: The name of the attribute to update.
        :param new_value: The new value to assign to the attribute.
        """
        if attribute_name in self.agent_data:
            self.agent_data[attribute_name] = new_value
        else:
            raise AgentCustomizationError(f"Attribute {attribute_name} not found in agent data.")

    def apply_customization(self, customization_options):
        """
        Apply a set of customization options to the agent.

        :param customization_options: A dictionary of attribute names and their new values.
        """
        for attribute, value in customization_options.items():
            try:
                self.update_attribute(attribute, value)
            except AgentCustomizationError as e:
                print(f"Error applying customization: {e}")

    def save_customizations(self):
        """
        Save the customizations to the agent's profile. This method should be implemented
        to interact with the database or storage system where the agent's data is kept.
        """
        # Code logic to save customizations to a persistent storage system.
        # For demonstration purposes, the following lines simulate interaction with a database.
        database.update_agent_profile(self.agent_data['id'], self.agent_data)


def customize_agent(agent_id, customization_options):
    """
    Function to customize an agent identified by its unique ID.

    :param agent_id: The unique identifier of the agent to be customized.
    :param customization_options: A dictionary containing the customization details.
    """
    # Fetch the agent's current data from the database or storage system.
    # For demonstration purposes, the following lines simulate interaction with a database.
    agent_data = database.fetch_agent_data(agent_id)
    if not agent_data:
        raise AgentCustomizationError(f"Could not fetch data for agent with ID {agent_id}.")

    # Ensure 'id' attribute is present in the agent_data
    if 'id' not in agent_data:
        agent_data['id'] = agent_id

    # Initialize the customizer with the agent's data.
    customizer = AgentCustomizer(agent_data)

    # Apply the customizations.
    customizer.apply_customization(customization_options)

    # Save the customizations.
    customizer.save_customizations()

    print(f"Agent {agent_id} has been customized successfully.")
