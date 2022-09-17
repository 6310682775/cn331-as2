from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    student_id = models.IntegerField(default=0,primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    year = models.IntegerField(validators=[MinValueValidator(1),
                                  MaxValueValidator(4)])
    def __str__(self):
        return f"{self.student_id} {self.first_name} {self.last_name} {self.year}"

class Subject(models.Model):
    sub_code = models.CharField(max_length=5,primary_key=True)
    sub_name = models.CharField(max_length=64)
    semester = models.IntegerField(validators=[MinValueValidator(1),
                                  MaxValueValidator(2)],default=1)
    credit = models.IntegerField(validators=[MinValueValidator(0),
                                  MaxValueValidator(3)],default=1)
    year = models.IntegerField(validators=[MinValueValidator(1),
                                  MaxValueValidator(4)])  
    amount = models.IntegerField(validators=[MinValueValidator(0),
                                  MaxValueValidator(9999)])
    amount_enrolled_student = models.IntegerField(validators=[MinValueValidator(0),
                                  MaxValueValidator(9999)],default=0)
    available = models.BooleanField(default=True)
    enrolled_student = models.ManyToManyField(User, blank=True, related_name="Subject")  

    def __str__(self):
        return f"{self.sub_code} {self.sub_name} {self.semester} {self.year} {self.amount} {self.available} { self.available}"

class Profile(models.Model):
    user = models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    year = models.IntegerField(validators=[MinValueValidator(1),
                                  MaxValueValidator(4)])  
