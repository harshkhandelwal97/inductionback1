from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def log(request):
    return render(request,'login.html')
def home(request):
    return render(request,'home.html')
def progress(request):
    return render(request,'progress.html')
def comment(request):
    return render(request,'comment.html')