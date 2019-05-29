from django.contrib import admin
from .models import UserInfo, Contacts, Introductions, Video, Schedules, StudyProcess, TypicalStudents, Classes, \
    Courses, Teachers

admin.site.register(UserInfo)
admin.site.register(Contacts)
admin.site.register(Introductions)
admin.site.register(Video)
admin.site.register(Schedules)
admin.site.register(StudyProcess)
admin.site.register(TypicalStudents)
admin.site.register(Classes)
admin.site.register(Courses)
admin.site.register(Teachers)
