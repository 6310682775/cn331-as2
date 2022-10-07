from django.test import TestCase
from main.models import Subject

from django.contrib.auth.models import User
# Create your tests here.
class SubjectTestCase(TestCase):

    def setUp(self):
        User1 = User.objects.create_user(username="student1", password="pass12345")
        User2 = User.objects.create_user(username="student2", password="pass12345")

        subject =Subject.objects.create(
            sub_code="CN361", sub_name="MICROPROCESSOR SYSTEMS DESIGN", semester=1,credit=3,amount=3,amount_enrolled_student=2)
        subject.enrolled_student.add(User1)
        subject.enrolled_student.add(User2)

    def test_subject_available(self):
        """ is_subject_available should be True """

        subject = Subject.objects.first()

        self.assertTrue(subject.is_subject_available())

    def test_subject_not_available(self):
        """ is_subject_available should be False """

        User1 = User.objects.create_user(username="student3", password="pass12345")
        User2 = User.objects.create_user(username="student4", password="pass12345")

        subject = Subject.objects.create(
            sub_code="CN360", sub_name="MICROPROCESSOR SYSTEMS DESIGN", semester=1,credit=3,amount=2,amount_enrolled_student=2)
        subject.enrolled_student.add(User1)
        subject.enrolled_student.add(User2)

        self.assertFalse(subject.is_subject_available())

