from django.shortcuts import get_object_or_404, render
from .models import Applicant, Employee



def login(request):
    return render(request, 'polls/login.html')

def signup(request):
    return render(request, 'polls/signup.html')

def signup2(request):
    return render(request, 'polls/signup2.html')

def search(request, applicant_id):
    applicant = get_object_or_404(Applicant, pk=applicant_id)
    return render(request, 'polls/search.html', {'applicant': applicant})

def home(request, applicant_id):
    applicant = get_object_or_404(Applicant, pk=applicant_id)
    return render(request, 'polls/home.html', {'applicant': applicant})

def report(request, applicant_id):
    applicant = get_object_or_404(Applicant, pk=applicant_id)
    return render(request, 'polls/report.html', {'applicant': applicant})

def profile(request, applicant_id):
    realid = decryptor(applicant_id)
    applicant = get_object_or_404(Applicant, pk=realid)
    employee = Employee.objects.get(employee_email = applicant.applicant_email)
    return render(request, 'polls/profile.html', {'applicant': applicant, 'employee':employee})
    
def decryptor (applicant_id):
    id = ((((applicant_id - 3) / 2) + 6) / 65) / 5
    return id





def encryptor(id):
    newid = ((((id * 5) * 65) - 6) * 2) + 3