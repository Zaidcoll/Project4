from django.shortcuts import render,redirect, reverse, HttpResponse
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm
#import the login required annotation
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'accounts/index.html')

#logout function
def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(index)
    
def login(request):
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            #check if username and password matches
            user = auth.authenticate(username = request.POST['username'],password = request.POST['password'])
            if user:
                auth.login(user = user, request = request)
                return redirect(index)
                                     
        else:
            pass
            
    else:
        form = UserLoginForm()
        return render(request,'accounts/login.html',{
            'form':form
        })

@login_required
def profile(request):
    return HttpResponse('Profile')
    
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            #check if username and password matches
            user = auth.authenticate(username=request.POST['username'],password=request.POST['password1'])
            if user:
                #login the user
                auth.login(user=user,request=request)
                messages.success(request,"You have registered successfully")
            else:
                messages.error(request,'You failed to register')
            return redirect(reverse('index'))
        else:
            return render(request,'accounts/register.html',{
                'form':form
            })
    else:
        register_form = UserRegistrationForm()
        return render(request, 'accounts/register.html',{
            'form':register_form
        })