from django import forms
from .models import Applicant, Employee, Message, Job, Company
from datetime import datetime



#create the form for signing up as an applicant
class SignUpForm(forms.ModelForm):
    applicant_email = forms.EmailField(label='Email', required=True, max_length=100)
    applicant_password = forms.CharField(label='Password', required=True, max_length=100, widget=forms.PasswordInput)
    applicant_name = forms.CharField(label = 'First Name', required =True, max_length=100)
    applicant_last_name = forms.CharField(label = "Last Name", required=True, max_length=100)

    class Meta:
        model = Applicant
        fields = ('applicant_email','applicant_password','applicant_name','applicant_last_name',)
    

#create the form for signing up as an employee
class SignUpForm2(forms.Form):
    employee_company = forms.CharField(label='Company Name', required=True, max_length=100)
    is_employer = forms.CharField(label="Are you an employer?", required=True, max_length=100)

#create the form for edit profile as an applicant
class editProfileForm(forms.ModelForm):
    applicant_email = forms.EmailField(label='Email', required=True, max_length=100)
    applicant_name = forms.CharField(label = 'First Name', required=True, max_length=100)
    applicant_last_name = forms.CharField(label = 'Last Name', required=True, max_length=100)
    applicant_address = forms.CharField(label = 'Address', required=False, max_length=100)

    class Meta: 
        model = Applicant
        fields = ('applicant_email', 'applicant_name', 'applicant_last_name', 'applicant_address',)

#create the form for loging in 
class LoginForm(forms.ModelForm):
    applicant_email = forms.EmailField(label='Email', required=True, max_length=100)
    applicant_password = forms.CharField(label='Password', required=True, max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = Applicant
        fields = ('applicant_email','applicant_password',)

class MessageForm(forms.Form):
    receiver_email = forms.CharField(label='Enter the Receiver\'s Email', required=True, max_length=100)
    message = forms.CharField(label='Your Message', required = True, max_length=500)

class SearchJobForm(forms.Form):
    search = forms.CharField(required=True, max_length=100, label="Search Job or Qualifications")

class ApplyForm(forms.Form):
    job_id = forms.IntegerField(label="Enter the Job ID for a job you have not already applied to:")

class AcceptForm(forms.Form):
    applicant_id = forms.IntegerField(label='Enter the applicant ID that you wish to hire:')

class SearchApplicantForm(forms.Form):
    search = forms.CharField(label='Search Applicant by Last Name or Resume Qualities', max_length=100, required=True)

class ResumeForm(forms.Form):
    applicant_resume = forms.CharField(label='Update or Enter Your Resume', required=True, max_length=1000)

    class Meta: 
        model = Applicant 
        fields = ('applicant_resume',)

class PostJobForm(forms.ModelForm):
    job_title = forms.CharField(label='Enter the Job Title', required=True, max_length=100)
    job_qualifications = forms.CharField(label='Enter the Qualifications for the Job', required=True, max_length=100)
    job_date = forms.DateTimeField(label='Enter the Job\'s Posting Date', required=True, initial = datetime.now())
    job_company = forms.ModelChoiceField(label='Enter the Job\'s Company', required=True, queryset = Company.objects.all() )

    class Meta:
        model = Job
        fields = ('job_title', 'job_qualifications', 'job_date', 'job_company')
        