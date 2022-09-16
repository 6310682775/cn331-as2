from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Subject , Student
from django.contrib import messages

# Create your views here.
@login_required(login_url="/login")
def home(request):

    return render(request, 'main/home.html')

@login_required(login_url="/login")
def enrollSub(request):
    subject_list = Subject.objects.all()
    return render(request, 'main/enrollSub.html',  {'subject_list': subject_list,
    "not_enroll_subject": Subject.objects.exclude(enrolled_student = Student.objects.get(pk=int(request.user.username))
)})

@login_required(login_url="/login")
def enroll_subject(request, sub_code):
    if request.method == "POST":
        student = Student.objects.get(pk=int(request.user.username))
        subject = Subject.objects.get(pk=sub_code)
        subject.enrolled_student.add(student)
        subject.amount = subject.amount - 1
        subject.save()
        messages.success(request, "enrolled")
        return redirect("/enrollSub")

@login_required(login_url="/login")
def drop(request, sub_code):
    if request.method == "POST":
        student = Student.objects.get(pk=int(request.user.username))
        subject = Subject.objects.get(pk=sub_code)
        subject.enrolled_student.remove(student)
        subject.amount = subject.amount + 1
        subject.save()
        messages.success(request, "dropped")
        return redirect("/enrolled")


@login_required(login_url="/login")
def enrolled(request):
    subject_list = Subject.objects.all()
    return render(request, 'main/enrolled.html',  {'subject_list': subject_list,
    "enrolled_subject": Subject.objects.filter(enrolled_student = Student.objects.get(pk=int(request.user.username))
)})