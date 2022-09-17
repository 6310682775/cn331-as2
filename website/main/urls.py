from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('enrollSub', views.enrollSub, name='enrollSub'),
    path('enrollSub/<str:sub_code>', views.enroll_subject, name='enroll_subject'),
    path('enrolled', views.enrolled, name='enrolled'),
    path('enrolled/<str:sub_code>', views.drop, name='drop'),
]