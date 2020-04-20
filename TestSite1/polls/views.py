from django.shortcuts import get_object_or_404, render, redirect
from .models import Applicant, Employee, Company, Job, Message
from .forms import SignUpForm, SignUpForm2, editProfileForm, LoginForm, MessageForm, SearchJobForm, SearchApplicantForm, ApplyForm
from django.contrib import messages
from django.db.models import Q, Count
from django.http import *




def login(request):
    #handles once the login form is submitted
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['applicant_email']
            password = form.cleaned_data['applicant_password']
            if Applicant.objects.filter(applicant_email = email).exists():
                q = Applicant.objects.get(applicant_email = email)
                realId = ((((q.id * 59)+36)*120)-14)*298
                if q.applicant_password == password:
                    return redirect('/home/'+str(realId))
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
    #handles once the signup form is submitted
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['applicant_email']
            password = form.cleaned_data['applicant_password']
            firstName = form.cleaned_data['applicant_name']
            lastName = form.cleaned_data['applicant_last_name']
            q = Applicant.objects.get(applicant_email = email)
            realId = ((((q.id * 59)+36)*120)-14)*298
        return redirect('/home/'+str(realId))
    else:
        form = SignUpForm()
        return render(request, 'polls/signup.html', {'form':form})

def signup2(request):
    #handles once the signup form is submitted
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
                realId = ((((q.id * 59)+36)*120)-14)*298
            return redirect('/home/'+str(realId))
        else:
            form1 = SignUpForm()
            form2 = SignUpForm2()
            return render(request, 'polls/signup2.html', {'form1':form1, 'form2':form2})
    else:
        form1 = SignUpForm()
        form2 = SignUpForm2()
        return render(request, 'polls/signup2.html', {'form1':form1, 'form2':form2})

def search(request, applicant_id):
    realId = decrypt(applicant_id)
    applicant = get_object_or_404(Applicant, pk=realId)
    job_list = Job.objects.order_by('job_title')[:5]
    applicant_list = Applicant.objects.order_by('applicant_last_name')[:5]

    #handles searching for jobs
    if request.method == 'POST':
        if 'searchjobform' in request.POST:
            search = request.POST['search']
            form1 = SearchJobForm(request.POST)
            if form1.is_valid():
                job_results = Job.objects.filter(Q(job_title__icontains = search) | Q(job_qualifications__icontains = search))
                if job_results:
                    #checks to see if applicant is employer because it will not display if they are not
                    try:
                        form2 = SearchApplicantForm()
                        form3= ApplyForm()
                        employee = Employee.objects.get(employee_email = applicant.applicant_email)
                        return render(request, 'polls/search.html', {'applicant': applicant, 'applicant_list':applicant_list, 'form1':form1, 'form3':form3, 'form2':form2, 'employee':employee, 'job_list': job_list, 'job_results': job_results})
                    except Employee.DoesNotExist:
                        return render(request, 'polls/search.html', {'applicant': applicant, 'applicant_list':applicant_list, 'form1': form1, 'form3':form3, 'form2':form2, 'job_list': job_list, 'job_results': job_results})
        elif 'searchapplicantform' in request.POST:
            search = request.POST['search']
            form2 = SearchApplicantForm(request.POST)
            if form2.is_valid():
                applicant_results_priority = Applicant.objects.filter(Q(applicant_last_name = search) | Q(applicant_resume__icontains = search))
                if applicant_results:
                    try:
                        form1=SearchJobForm()
                        form3=ApplyForm()
                        employee = Employee.objects.get(employee_email = applicant.applicant_email)
                        return render(request, 'polls/search.html', {'applicant': applicant, 'form3':form3, 'form2':form2, 'applicant_list':applicant_list, 'form1':form1, 'employee':employee, 'job_list': job_list, 'job_results': job_results})
                    except Employee.DoesNotExist:
                        return render(request, 'polls/search.html', {'applicant': applicant, 'form3':form3, 'form2':form2, 'applicant_list':applicant_list, 'form1': form1, 'job_list': job_list, 'job_results': job_results})
        elif 'applyform' in request.POST:
            form3 = ApplyForm(request.POST)
            if form3.is_valid():
                job_id = form3.cleaned_data['job_id']
                q = Job.objects.get(pk = job_id)
                applicant.applicant_job.add(q)
            try:
                employee = Employee.objects.get(employee_email = applicant.applicant_email)
                return redirect('/search/'+str(applicant_id))
            except Employee.DoesNotExist:
                return redirect('/search/'+str(applicant_id))

    #checks to see if applicant is employer because it will not display if they are not
    try:
        form3 = ApplyForm()
        form1 = SearchJobForm()
        form2 = SearchApplicantForm()
        employee = Employee.objects.get(employee_email = applicant.applicant_email)
        form1 = SearchJobForm()
        return render(request, 'polls/search.html', {'applicant': applicant, 'applicant_list':applicant_list, 'form2':form2, 'form3': form3, 'form1':form1, 'employee':employee, 'job_list': job_list})
    except Employee.DoesNotExist:
        form3 = ApplyForm()
        form1 = SearchJobForm()
        form2 = SearchApplicantForm()
        return render(request, 'polls/search.html', {'applicant': applicant,'applicant_list':applicant_list, 'form2':form2, 'form3': form3, 'form1':form1, 'job_list': job_list})

def home(request, applicant_id):
    realId = decrypt(applicant_id)
    applicant = get_object_or_404(Applicant, pk=realId)
    #check to see if applicant is an administrator because it will not display reports option if they are not
    try:
        employee = Employee.objects.get(employee_email = applicant.applicant_email)
        return render(request, 'polls/home.html', {'applicant': applicant, 'employee':employee})
    except Employee.DoesNotExist:
        return render(request, 'polls/home.html', {'applicant': applicant})

def report(request, applicant_id):
    realId = decrypt(applicant_id)
    applicant = get_object_or_404(Applicant, pk=realId)
    id = Applicant.objects.get(id=realId)
    applied = Applicant.objects.filter(applicant_job__isnull=False)
    company_id = Company.objects.get(employee__employee_email=id)
    company_all = Company.objects.filter(employee__employee_email__in=list(applied))
    job_id = Job.objects.filter(job_company=company_id)
    j = Job.objects.all()
    a = Applicant.objects.all()
    c = Company.objects.all()
    e = Employee.objects.all()

    job_data = {
        "job_id": j
    }

    company_data = {
        "company_id": c
    }

    employee_data = {
        "employee_id": e
    }

    applicant_data = {
        "applicant_id": a
    }

    for a in Applicant.objects.filter(applicant_job__in=job_id).values_list('applicant_name', 'applicant_last_name',
                                                                            'applicant_job', 'application_status'):
        print(a)

    for c in Company.objects.filter(company_name__in=company_all).values_list('company_name',
                                                                              count=Count('company_name')):
        print(c)

    return render(request, 'polls/report.html', {'applicant': applicant}, job_data, company_data, employee_data, applicant_data)

def profile(request, applicant_id):
    realId = decrypt(applicant_id)
    applicant = get_object_or_404(Applicant, pk=realId)
    #handles what happens once a message is sent
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            receiver_email = form.cleaned_data['receiver_email']
            message = form.cleaned_data['message']
            sender_email = applicant.applicant_email
            t = Message(sender_email=sender_email, receiver_email=receiver_email, message=message)
            t.save()
        return redirect('/profile/'+str(applicant_id))
    #checks if they are an employee or employer or if they have messages because if they are not some things will not be displayed
    try:
        employee = Employee.objects.get(employee_email = applicant.applicant_email)
        form = MessageForm()
        try:
            messages = Message.objects.filter(receiver_email = applicant.applicant_email)
            form = MessageForm()
            return render(request, 'polls/profile.html', {'applicant': applicant, 'employee':employee, 'messages': messages, 'form':form})
        except Message.DoesNotExist:
            form = MessageForm()
            return render(request, 'polls/profile.html', {'applicant': applicant, 'employee':employee, 'form':form})
    except Employee.DoesNotExist:
        try:
            form = MessageForm()
            messages = Message.objects.filter(receiver_email = applicant.applicant_email)
            return render(request, 'polls/profile.html', {'applicant': applicant, 'messages': messages, 'form':form})
        except Message.DoesNotExist:
            form = MessageForm()
            return render(request, 'polls/profile.html', {'applicant': applicant, 'form':form})

def editProfile(request, applicant_id):
    realId = decrypt(applicant_id)
    applicant = get_object_or_404(Applicant, pk=realId)
    update = Applicant.objects.get(id = realId)
    #handles the changes to the profile once the editprofile page is submitted
    if request.method == 'POST':
        form = editProfileForm(request.POST, instance=update)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['applicant_email']
            firstName = form.cleaned_data['applicant_name']
            lastName = form.cleaned_data['applicant_last_name']
            address = form.cleaned_data['applicant_address']
            q = Applicant.objects.get(applicant_email = email)
            realId = decrypt(q.id)
        return redirect('/profile/'+str(applicant_id))
    else:
        form = editProfileForm(instance=update)
        return render(request, 'polls/editProfile.html', {'applicant': applicant, 'form':form})


#encryption (id * 59) + 36 ) * 120 ) - 14 ) * 298)

def decrypt(did):
    decryptid = did
    realid = ((((decryptid / 298) + 14) / 120) - 36) / 59
    return realid


