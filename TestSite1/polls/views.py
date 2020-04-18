from django.shortcuts import get_object_or_404, render
from .models import Applicant, Employee



def login(request):
    return render(request, 'polls/login.html')

def signup(request):
    return render(request, 'polls/signup.html')

def signup2(request):
    return render(request, 'polls/signup2.html')

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
    employee = Employee.objects.get(employee_email = applicant.applicant_email)
    return render(request, 'polls/profile.html', {'applicant': applicant, 'employee':employee})