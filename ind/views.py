from django.shortcuts import render,redirect,HttpResponse     
from django.contrib.auth.models import User
from .models import Member
from datetime import date 
def log(request):
    return render(request,'login.html')
def home(request):
    return render(request,'home.html')
def progress(request):
     return render(request,'progress.html')
    
def comment(request):
    return render(request,'comment.html')

def redirect_to_progress(request):
    return render(request,'progress.html')
# def logged(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         print(email)
#         print(password)
#         user = authenticate(request,email = email,password = password)
#         print(user)
#         if user is not None and user.is_active:
#             login(request,user)
#             return redirect('home.html')
#         else:
#             return HttpResponse("credentials are invalid")
#     # return render(request,'home.html')
#     return render(request,'login.html')

def logged(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return redirect('home')
            else:
                return HttpResponse("Invalid password")
        except User.DoesNotExist:
            return HttpResponse("User does not exist")

    return render(request, 'login.html')

def saveprogress(request):
        # Assuming you have a form with fields 'description', 'image1', 'image2', and 'image3'
        description = request.POST.get('progress')
        date = request.POST.get('date')
        # image1 = request.FILES.get('image1')
        # image2 = request.FILES.get('image2')
        # image3 = request.FILES.get('image3')
        
        if description and  date:
            progress = Member()
            progress.date = date
            progress.description = description
            # print(progress.description)
            # progress.image1 = image1
            # progress.image2 = image2
            # progress.image3 = image3
            
            progress.save()

            # Redirect to the home page
            return redirect('home')
        else:
            return HttpResponse("error occured")

      