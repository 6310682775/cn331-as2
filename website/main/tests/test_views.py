from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from django.db.models import Max
from main.models import Subject
import json
from django.contrib.auth.models import User

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')

    def test_project_home_GET(self):
        response = self.client.get(reverse('education:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/home.html')

    def test_project_enrolled_GET(self):
        response = self.client.get(reverse('education:enrolled'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/enrolled.html')

    def test_project_enrollsub_GET(self):
        response = self.client.get(reverse('education:enrollSub'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/enrollSub.html')

    def test_enroll_student_success(self):
        """ test """
        self.subject =Subject.objects.create( sub_code="CN361", sub_name="MICROPROCESSOR SYSTEMS DESIGN", semester=1,credit=3,amount=1)
        client = Client()
        client.login(username='john', password='johnpassword')
        S = Subject.objects.get(pk="CN361") 

        client.post(reverse('education:enroll_subject', args=(S.sub_code,)))
        self.assertEqual(S.enrolled_student.count(), 1)

    def test_enroll_student_but_subject_is_full(self):
        """test เมื่อ subjectfull จะ ไม่add user ลงใน enrolled_subject เพิ่ม อาจเกิดเหตุการนี้ขึ้นเมื่อเข้าจากหลายuser"""
        self.subject =Subject.objects.create( sub_code="CN362", sub_name="MICROPROCESSOR SYSTEMS DESIGN", semester=1,credit=3,amount=1)
        User1 = User.objects.create_user(username="student4", password="pass12345")
        S = Subject.objects.get(pk="CN362")
        S.enrolled_student.add(User1)
        S.save()

        client = Client()
        client.login(username='john', password='johnpassword')

        client.post(reverse('education:enroll_subject', args=(S.sub_code,)))
        self.assertEqual(S.enrolled_student.count(), 1)

    def test_drop_student_success(self):
        """test เมื่อ drop User ที่login ขณะนั้น เงื่อนไขของความสำเร็จ คือ user ใน enrolled_student ถูก remove ออกและเมื่อนับจะมีค่าเท่ากับ0"""
        self.subject =Subject.objects.create( sub_code="CN363", sub_name="MICROPROCESSOR SYSTEMS DESIGN", semester=1,credit=3,amount=1)
        S = Subject.objects.get(pk="CN363")
        U = User.objects.get(username='john')
        S.enrolled_student.add(U)
        S.save()

        client = Client()
        client.login(username='john', password='johnpassword')

        client.post(reverse('education:drop', args=(S.sub_code,)))
        self.assertEqual(S.enrolled_student.count(), 0)