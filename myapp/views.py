from .models import*
from random import *
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def emergency_contact(request):
    msg='YOUR DETAIL IS SAVE SUCCESSFULLY'
    if request.method =='POST':
        name =  request.POST['name']
        mobile = request.POST['mobile']
        occupation = request.POST['occupation']
        Emergency_Contact.objects.create(name=name,mobile=mobile,occupation=occupation)
        many=Emergency_Contact.objects.all()

        return render(request,'emergencycontact.html',{'msg':msg,'many':many})
    
    else:
        many=Emergency_Contact.objects.all()
        return render(request,'emergencycontact.html',{'many':many}) 






def profile(request):
    msg='PROFILE UPDATE SUCCESSFULLY'
    uid=Users.objects.get(email=request.session['email'])
    if request.method=='POST':
        uid.name = request.POST['name']
        uid.mail = request.POST['email']
        uid.mobile = request.POST['mobile']
        uid.address=request.POST['address']
        uid.password=request.POST['password']
        uid.save()
        return render(request,'profile.html',{'msg':msg,'uid':uid})
    else:
        return render(request,'profile.html',{'uid':uid})

def register(request):
    if request.method == 'POST':
        try:
            Users.objects.get(email = request.POST['email'])
            msg = "Your Email Is Already Exits"
            return render(request,'register.html',{'msg' : msg})
        except:
                otp = randrange(1000,9999) 
                subject = 'DIGITAL SOCIETY VERIFICATION CODE'
                message = f'Hello User your OTP is : {otp}'
                email_from=settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email'], ]
                send_mail(subject,message,email_from,recipient_list)
                global temp
                temp = {
                    'name' : request.POST['name'],
                    'email' : request.POST['email'],
                    'address' : request.POST['address'],
                    'mobile' : request.POST['mobile'],
                    'password' : request.POST['password'],
                    'otp' : otp
                }
                
                return render(request,'otp.html',{'otp':otp})
            
    return render(request,'register.html')

def otp(request):
    if request.method == 'POST':
        if request.POST['otp'] == request.POST['uotp']:
            global temp
            Users.objects.create(
                name = temp['name'],
                email = temp['email'],
                address = temp['address'],
                mobile = temp['mobile'],
                password = temp['password']
            )
            msg = 'User Created'
            del temp
            return render(request,'register.html',{'msg' : msg})
        else:
            msg = 'Otp Does Not Match'
            return render(request,'otp.html',{'msg' : msg,'otp' : request.POST['otp']})
    return render(request,'otp.html')


def signin(request):
    if request.method=='POST':
        try:
            uid=Users.objects.get(email=request.POST['email'])
            
            if request.POST['password']== uid.password:
                request.session['email']=request.POST['email']
                print(request.session['email'])
                return render(request,'index.html',{'uid':uid})
            else:
                return render(request,'sign-in.html',{'msg':'INVALID DATA'})
        except:
            msg='GO AND SIGNUP FIRST'
            return render(request,'sign-in.html',{'msg':msg})
    return render(request,'sign-in.html')

def logout(request):
    del request.session['email']
    return render(request,'sign-in.html')
