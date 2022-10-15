from django.shortcuts import render, HttpResponse

# Create your views here.
def home_page(request):
    return render(request,'home.html')

def about_page(request):
    return render(request,'about.html')

def login_page(request):
    return render(request,'login.html')

def signup_page(request):
    return render(request,'signup.html')

def logo(request):
    return render(request,'logo.html')
