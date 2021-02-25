from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        ("\n"
         "    was published_recently() returns False for questions whose pub_date\n"
         "    ")
    time = timezone.now() + datetime.timedelta(days=30)
    future_question = Question(pub_date=time)
    TestCase.assertIs(future_question.was_published_recently(),
                  False)
