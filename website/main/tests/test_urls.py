from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import home, enrollSub, enroll_subject, drop, enrolled

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('education:home')
        self.assertEqual(resolve(url).func, home)
    
    def test_enrollSub_url_is_resolved(self):
        url = reverse('education:enrollSub')
        self.assertEqual(resolve(url).func, enrollSub)

    def test_enroll_subject_url_is_resolved(self):
        url = reverse('education:enroll_subject', args=['test'])
        self.assertEqual(resolve(url).func, enroll_subject)

    def test_enrolled_url_is_resolved(self):
        url = reverse('education:enrolled')
        self.assertEqual(resolve(url).func, enrolled)
    
    def test_drop_url_is_resolved(self):
        url = reverse('education:drop', args=['test'])
        self.assertEqual(resolve(url).func, drop)