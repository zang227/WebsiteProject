from django.shortcuts import render



def login(request):
    return render(request, 'polls/login.html')

def signup(request):
    return render(request, 'polls/signup.html')

def signup2(request):
    return redner(request, 'polls/signup2.html')

def search(request):
    return render(request, 'polls/search.html')

def home(request):
    return render(request, 'polls/home.html')

def report(request):
    return render(request, 'polls/report.html')

def profile(request):
    return render(request, 'polls/profile.html')
