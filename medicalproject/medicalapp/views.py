from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import medicine



# Create your views here.
def index(request):
    obj=medicine.objects.all()
    return render(request,'index.html',{'med':obj})

def about(request):
    return render(request,'about.html')

def Medicine(request):
    med=medicine.objects.all()
    return render(request,'medicine.html',{'med':med})

def endpage(request):
    return render(request,'endpage.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None :
            auth.login(request,user)
            return redirect('medicalapp:booking')
        else:
            messages.info(request,"INVALID CREDENTIALS")
            return redirect('medicalapp:login')
    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confpass = request.POST['confpass']
        if password == confpass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"USERNAME TAKEN")
                return redirect('medicalapp:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "EMAIL TAKEN")
                return redirect('medicalapp:register')
            else:
                user = User.objects.create_user(username=username,password=password,email=email)
                user.save();
                return redirect('medicalapp:login')

        else:
            messages.info(request,"PASSWORD not same")
            return redirect('medicalapp:register')

        return redirect('/')

    return render(request,"registration.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def booking(request):
    if request.method == 'POST':
        username = request.POST['username']
        if User.objects.filter(username=username).exists():
            return redirect('medicalapp:endpage')

        else:
            messages.info(request,'ENTER VALID USERNAME')
    return render(request,'booking.html')