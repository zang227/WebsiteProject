from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
    company_description = models.CharField(max_length=200)
    company_association = models.ForeignKey('Association', null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.company_name
    
class Association(models.Model):
    association_name = models.CharField(max_length=100)
    association_address = models.CharField(max_length=100)
    association_description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.association_name

class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_last_name = models.CharField(max_length=100)
    employee_email = models.CharField(max_length=100)
    employee_address = models.CharField(max_length=100)
    employee_resume = models.CharField(max_length=500)
    employee_company = models.ForeignKey('Company', null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.employee_email

class Job(models.Model):
    job_title = models.CharField(max_length=100)
    job_date = models.DateTimeField('date posted')
    job_status = models.CharField(max_length=100)
    job_company = models.ForeignKey('Company', null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.job_title

class Applicant(models.Model):
    applicant_name = models.CharField(max_length=100)
    applicant_last_name = models.CharField(max_length=100)
    applicant_email = models.CharField(max_length=100)
    applicant_resume = models.CharField(max_length=500)
    application_status = models.CharField(max_length=100)
    applicant_job = models.ForeignKey('Job', null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.applicant_email