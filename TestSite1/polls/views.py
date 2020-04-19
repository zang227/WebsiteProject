from django.shortcuts import get_object_or_404, render, redirect
from .models import Applicant, Employee, Company
from .forms import SignUpForm, SignUpForm2



def login(request):
    return render(request, 'polls/login.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # email = form.cleaned_data['applicant_email']
            # password = form.cleaned_data['applicant_password']
            # firstName = form.cleaned_data['applicant_name']
            # lastName = form.cleaned_data['applicant_last_name']
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

def search(request):
    return render(request, 'polls/search.html')

def home(request, applicant_id):
    applicant = get_object_or_404(Applicant, pk=applicant_id)
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
    
