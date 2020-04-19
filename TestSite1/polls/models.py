from django.db import models

#Company model
class Company(models.Model):
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
    company_description = models.CharField(max_length=1000)
    company_association = models.ForeignKey('Association', null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.company_name

#Association model    
class Association(models.Model):
    association_name = models.CharField(max_length=100)
    association_address = models.CharField(max_length=100)
    association_description = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.association_name

#Employee model
class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_last_name = models.CharField(max_length=100)
    employee_email = models.CharField(max_length=100)
    is_employer = models.CharField(max_length=100)
    employee_company = models.ForeignKey('Company', null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.employee_email

#Job model
class Job(models.Model):
    job_title = models.CharField(max_length=100)
    job_qualifications = models.CharField(max_length=1000)
    job_date = models.DateTimeField('date posted')
    job_status = models.CharField(max_length=100)
    job_company = models.ForeignKey('Company', null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.job_title

#Applicant model
class Applicant(models.Model):
    applicant_name = models.CharField(max_length=100)
    applicant_last_name = models.CharField(max_length=100)
    applicant_email = models.CharField(max_length=100)
    applicant_password = models.CharField(max_length=100)
    applicant_address = models.CharField(max_length=100)
    applicant_resume = models.CharField(max_length=1000)
    application_status = models.CharField(max_length=100)
    applicant_job = models.ForeignKey('Job', null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.applicant_email

#Message model
class Message(models.Model):
    sender_email = models.CharField(max_length=100)
    receiver_email = models.CharField(max_length=100)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.message
