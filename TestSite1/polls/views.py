from django.shortcuts import get_object_or_404, render, redirect
from .models import Applicant, Employee, Company, Job
from .forms import SignUpForm, SignUpForm2, editProfileForm, LoginForm
from django.contrib import messages



def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['applicant_email']
            password = form.cleaned_data['applicant_password']
            if Applicant.objects.filter(applicant_email = email).exists():
                q = Applicant.objects.get(applicant_email = email)
                if q.applicant_password == password:
                    return redirect('/home/'+str(q.id))
                else:
                    messages.error(request, 'Your password is incorrect.')
                    return redirect('login-home')
            else:
                messages.error(request, 'Your email is not correct. If you are a new user, click sign up to sign up')
                return redirect('login-home')
    else:
        form = LoginForm()
        return render(request, 'polls/login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['applicant_email']
            password = form.cleaned_data['applicant_password']
            firstName = form.cleaned_data['applicant_name']
            lastName = form.cleaned_data['applicant_last_name']
            q = Applicant.objects.get(applicant_email = email)
        return redirect('/home/'+str(q.id))
    else:
        form = SignUpForm()
        return render(request, 'polls/signup.html', {'form':form})

def signup2(request):
    if request.method == 'POST':
        form1 = SignUpForm(request.POST)
        form2 = SignUpForm2(request.POST)
        if form1.is_valid():
            form1.save()
            if form2.is_valid():
                email = form1.cleaned_data['applicant_email']
                password = form1.cleaned_data['applicant_password']
                firstName = form1.cleaned_data['applicant_name']
                lastName = form1.cleaned_data['applicant_last_name']
                company = form2.cleaned_data['employee_company']
                is_employer = form2.cleaned_data['is_employer']
                r = Company.objects.get(company_name = company)
                t = Employee(employee_name = firstName, employee_last_name=lastName, employee_email=email, employee_company=r, is_employer=is_employer)
                t.save()
                q = Applicant.objects.get(applicant_email = email)
            return redirect('/home/'+str(q.id))
        else:
            form1 = SignUpForm()
            form2 = SignUpForm2()
            return render(request, 'polls/signup2.html', {'form1':form1, 'form2':form2})
    else:
        form1 = SignUpForm()
        form2 = SignUpForm2()
        return render(request, 'polls/signup2.html', {'form1':form1, 'form2':form2})

def search(request, applicant_id):
    applicant = get_object_or_404(Applicant, pk=applicant_id)
    job_list = Job.objects.order_by('job_title')[:5]
    try:
        employee = Employee.objects.get(employee_email = applicant.applicant_email)
        return render(request, 'polls/search.html', {'applicant': applicant, 'employee':employee, 'job_list': job_list})
    except Employee.DoesNotExist:
        return render(request, 'polls/search.html', {'applicant': applicant, 'job_list': job_list})

def home(request, applicant_id):
    applicant = get_object_or_404(Applicant, pk=applicant_id)
    try:
        employee = Employee.objects.get(employee_email = applicant.applicant_email)
        return render(request, 'polls/home.html', {'applicant': applicant, 'employee':employee})
    except Employee.DoesNotExist:
        return render(request, 'polls/home.html', {'applicant': applicant})

def report(request, applicant_id):
    applicant = get_object_or_404(Applicant, pk=applicant_id)
    return render(request, 'polls/report.html', {'applicant': applicant})

def profile(request, applicant_id):
    applicant = get_object_or_404(Applicant, pk=applicant_id)
    try:
        employee = Employee.objects.get(employee_email = applicant.applicant_email)
        return render(request, 'polls/profile.html', {'applicant': applicant, 'employee':employee})
    except Employee.DoesNotExist:
        return render(request, 'polls/profile.html', {'applicant': applicant})

def editProfile(request, applicant_id):
    applicant = get_object_or_404(Applicant, pk=applicant_id)
    update = Applicant.objects.get(id = applicant_id)

    if request.method == 'POST':
        form = editProfileForm(request.POST, instance=update)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['applicant_email']
            firstName = form.cleaned_data['applicant_name']
            lastName = form.cleaned_data['applicant_last_name']
            address = form.cleaned_data['applicant_address']
            q = Applicant.objects.get(applicant_email = email)
        return redirect('/profile/'+str(q.id))
    else:
        form = editProfileForm(instance=update)
        return render(request, 'polls/editProfile.html', {'applicant': applicant, 'form':form})

    
