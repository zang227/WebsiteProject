from django.contrib import admin

from .models import Company, Association, Employee, Job, Applicant, Message

admin.site.register(Company)
admin.site.register(Association)
admin.site.register(Employee)
admin.site.register(Job)
admin.site.register(Applicant)
admin.site.register(Message)