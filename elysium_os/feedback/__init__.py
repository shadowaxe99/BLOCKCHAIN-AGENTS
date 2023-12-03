```python
from elysium_os.feedback.user_feedback import collect_user_feedback
from elysium_os.feedback.feedback_implementation import implement_feedback

class FeedbackManager:
    def __init__(self):
        self.feedback_records = []

    def collect_feedback(self, user_id, feedback_data):
        """
        Collect feedback from users and store it for further processing.

        :param user_id: Unique identifier for the user providing feedback.
        :param feedback_data: The content of the user's feedback.
        """
        feedback = collect_user_feedback(user_id, feedback_data)
        self.feedback_records.append(feedback)
        return feedback

    def process_feedback(self):
        """
        Process the collected feedback and implement necessary changes.
        """
        for feedback in self.feedback_records:
            implement_feedback(feedback)
            # Mark feedback as processed
            feedback['processed'] = True

    def get_unprocessed_feedback(self):
        """
        Retrieve all unprocessed feedback records.

        :return: List of unprocessed feedback records.
        """
        return [fb for fb in self.feedback_records if not fb.get('processed')]

# Instantiate the FeedbackManager to be used across the Elysium OS
feedback_manager = FeedbackManager()
```