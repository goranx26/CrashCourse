import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def setUp(self):
        """Create a survey and a set of responses for use in all test methods"""
        question = "What language did you first code in?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Basic', 'PHP', 'Pascal']


    def test_store_single_response(self):
        """tests that a single response is stored properly"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)


    def test_store_three_responses(self):
        """tests that three responses are properly stored"""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()

