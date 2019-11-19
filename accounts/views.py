from django.shortcuts import render,redirect, reverse, HttpResponse
from django.contrib import auth, messages
from .forms import UserLoginForm


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