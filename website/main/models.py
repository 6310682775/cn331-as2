from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.



class Subject(models.Model):
    sub_code = models.CharField(max_length=5,primary_key=True)
    sub_name = models.CharField(max_length=64)
    semester = models.IntegerField(validators=[MinValueValidator(1),
                                  MaxValueValidator(2)],default=1)
    credit = models.IntegerField(validators=[MinValueValidator(0),
                                  MaxValueValidator(3)],default=1)
    amount = models.IntegerField(validators=[MinValueValidator(0),
                                  MaxValueValidator(9999)])
    enrolled_student = models.ManyToManyField(User, blank=True, related_name="Subject")
    amount_enrolled_student = models.IntegerField(validators=[MinValueValidator(0),
                                  MaxValueValidator(9999)],default= 0)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.sub_code} {self.sub_name}  "

    def is_subject_available(self):
        return self.enrolled_student.count() < self.amount


class Profile(models.Model):
    user = models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    year = models.IntegerField(validators=[MinValueValidator(1),
                                  MaxValueValidator(4)]) 

    def __str__(self):
        return f"{self.user} {self.year}  " 
