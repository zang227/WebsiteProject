from django import forms
from .models import Applicant, Employee


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

        