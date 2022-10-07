from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Subject
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url="/login")
def home(request):
    subject_list = Subject.objects.all()
    return render(request, 'main/home.html',{'subject_list': subject_list})

@login_required(login_url="/login")
def enrollSub(request):
    subject_list = Subject.objects.all()
    return render(request, 'main/enrollSub.html',  {'subject_list': subject_list,
    "not_enroll_subject": Subject.objects.exclude(enrolled_student = User.objects.get(username=request.user.username)) ,
    "student_account" : User.objects.filter(username=request.user.username)})

@login_required(login_url="/login")
def enroll_subject(request, sub_code):
    if request.method == "POST":
        student = User.objects.get(username=request.user.username)
        subject = Subject.objects.get(pk=sub_code)
        if(subject.is_subject_available()):
            subject.enrolled_student.add(student)
        else:
            messages.error(request, "SUBJECT IS FULL")
            return redirect("/enrollSub")  

        if(student in subject.enrolled_student.all()):      
            subject.amount_enrolled_student = subject.amount_enrolled_student + 1
            subject.save()
            messages.success(request, "ENROLL SUCCESS")
            return redirect("/enrollSub")
        else:
            messages.error(request, "UNKNOWN ERROR PLEASE CONTACT ADMIN")
            return redirect("/enrollSub")

@login_required(login_url="/login")
def drop(request, sub_code):
    if request.method == "POST":
        student = User.objects.get(username=request.user.username)
        subject = Subject.objects.get(pk=sub_code)
        subject.enrolled_student.remove(student)

        if(student not in subject.enrolled_student.all()):      
            subject.amount_enrolled_student = subject.amount_enrolled_student - 1
            subject.save()
            messages.success(request, "DROP SUCCESS")
            return redirect("/enrolled")
        else:
            messages.error(request, "UNKNOWN ERROR PLEASE CONTACT ADMIN")
            return redirect("/enrolled")


@login_required(login_url="/login")
def enrolled(request):
    subject_list = Subject.objects.all()
    return render(request, 'main/enrolled.html',  {'subject_list': subject_list,
    "enrolled_subject": Subject.objects.filter(enrolled_student = User.objects.get(username=request.user.username)
)})

