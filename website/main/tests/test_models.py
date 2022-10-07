from django.test import TestCase
from main.models import Subject

from django.contrib.auth.models import User
# Create your tests here.
class SubjectTestCase(TestCase):

    def setUp(self):
        User.objects.create_user(username="student1", password="pass12345")
        Subject.objects.create(
            sub_code="CN361", sub_name="SUBJECT", semester=1,credit=3,amount=1)

    def test_subject_available(self):
        """ is_subject_available should be True """

        subject = Subject.objects.first()
        self.assertTrue(subject.is_subject_available())

    def test_subject_not_available(self):
        """ is_subject_available should be False """

        user = User.objects.get(username="student1")

        subject = Subject.objects.get(pk="CN361")
        subject.enrolled_student.add(user)

        self.assertFalse(subject.is_subject_available())

