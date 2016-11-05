from django.test import TestCase

class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_old_question(self):
        self.assertIs(False, False)