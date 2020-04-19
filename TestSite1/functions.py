from polls.models import Company, Association, Employee, Job, Applicant


def createJob(title, qual, jobdate, status, company):

    createjob = Job(job_title=title, job_qualifications=qual, job_date=jobdate, job_status=status, job_company=company)
    createjob.save()


def createEmployee(firstName, lastName, email, password, address, resume, status, job, employer,company):

    d3 = Employee(employee_name=firstName, employee_last_name=lastName, employee_email=email,
                  is_employer=employer, employee_company=company)
    d3.save()


def creatApplicant(firstName, lastName, email, password, address, resume, status, job):

    a1 = Applicant(applicant_name=firstName, applicant_last_name=lastName,
                   applicant_email=email, applicant_password=password,
                   applicant_address=address,
                   applicant_resume=resume,
                   application_status=status, applicant_job=job)
    a1.save()
