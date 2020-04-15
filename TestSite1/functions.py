from polls.models import Company, Association, Employee, Job, Applicant, Search_Committee

def create_Tim():
   q = Employee(employee_name="Timothy", employee_last_name="Steudlein", employee_email="Tsteud1@lsu.edu", employee_address="4441 Burbank Drive", employee_resume="Temp resume", employee_company=None)
   q.save()
   
def delete_Tim():
    q = Employee.objects.filter(employee_email="Tsteud1@lsu.edu")
    q.delete()