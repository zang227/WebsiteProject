from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
    company_description = models.CharField(max_length=200)
    company_employee = models.ForeignKey('Employee', null=True, on_delete=models.SET_NULL)
    company_job = models.ForeignKey('Job', null=True, on_delete=models.SET_NULL)
    
class Association(models.Model):
    association_name = models.CharField(max_length=100)
    association_address = models.CharField(max_length=100)
    association_description = models.CharField(max_length=200)
    association_company = models.ForeignKey('Company', null=True, on_delete=models.SET_NULL)

class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_last_name = models.CharField(max_length=100)
    employee_email = models.CharField(max_length=100)
    employee_address = models.CharField(max_length=100)
    employee_resume = models.CharField(max_length=500)
    employee_company = models.ForeignKey('Company', null=True, on_delete=models.SET_NULL)

class Job(models.Model):
    job_title = models.CharField(max_length=100)
    job_date = models.DateTimeField('date posted')
    job_status = models.CharField(max_length=100)
    job_company = models.ForeignKey('Company', null=True, on_delete=models.SET_NULL)
    job_applicant = models.ForeignKey('Applicant', null=True, on_delete=models.SET_NULL)
    job_search_committee = models.ForeignKey('Search_Committee', null=True, on_delete=models.SET_NULL)

class Applicant(models.Model):
    applicant_name = models.CharField(max_length=100)
    applicant_last_name = models.CharField(max_length=100)
    applicant_resume = models.CharField(max_length=500)
    application_status = models.CharField(max_length=100)

class Search_Committee(models.Model):
    SC_employee = models.ForeignKey('Employee', null=True, on_delete=models.SET_NULL)
    SC_job = models.ForeignKey('Job', null=True, on_delete=models.SET_NULL)