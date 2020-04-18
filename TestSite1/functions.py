from polls.models import Company, Association, Employee, Job, Applicant
from datetime import date

def create_Tim():
   q = Employee(employee_name="Timothy",employee_last_name="Steudlein",employee_email="Tsteud1@lsu.edu",employee_address="4441 Burbank Drive",employee_resume="Temp resume",employee_company=None)
   q.save()
   
def delete_Tim():
    q = Employee.objects.filter(employee_email="Tsteud1@lsu.edu")
    q.delete()
    
def insert_test_data():

    current = datetime.now()
    
    a = Company(company_name="Microsoft",company_address="1234 Road Drive",company_description="Best tech company in the world",company_association=None)
    b = Association(association_name="Big Tech Association",association_address="4321 Sunset Road",association_description="Biggest and best tech association in the world")
    c = Employee(employee_name="Timothy",employee_last_name="Steudlein",employee_email="Tsteud1@lsu.edu",employee_address="4441 Burbank Drive",employee_resume="Temp resume",employee_company=None)
    d = Job(job_title="Software Engineer",job_date=current,job_status="Open",job_company=None)
    e = Applicant(applicant_name="Timothy",applicant_last_name="Steudlein",applicant_email="Tsteud1@lsu.edu",applicant_resume="Temp resume",application_status="Approved",applicant_job=None)
    
    a.save()
    b.save()
    c.save()
    d.save()
    e.save()
    
    # then go into admin portal and manually set Foreign relationships!