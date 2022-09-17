from django.contrib import admin

# Register your models here.
from .models import Profile, Subject

# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
    filter_horizontal = ['enrolled_student']

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Profile)