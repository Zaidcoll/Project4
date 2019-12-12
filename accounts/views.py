from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm

# import in the login_required annonation
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "accounts/index.html")
    
"""
This is the logout function
"""
def logout(request):
    auth.logout(request)
    messages.success(request, "You have been logged out")
    return redirect(index)

"""
This is login function
"""
def login(request):
    """Returns the login page"""
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST) # populate the form from what the user has keyed in
        if login_form.is_valid():
            # attempt to check the username and password is valid
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            
            if user:
                # log in the user
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in")
                return redirect(reverse('catalog'))
            else:
                login_form.add_error(None, "Invalid username or password")
                return render(request, 'accounts/login.html', {
                  'form':login_form
                })

        
            
    else:
        form = UserLoginForm()
        return render(request, 'accounts/login.html', {
            'form':form
        })
        
@login_required
def profile(request):
    return HttpResponse("Profile")
    
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # check if the username and password matches
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                # actually log the user in
                auth.login(user=user, request=request)
                messages.success(request, "You have registered successful")
            else:
                messages.error(request, "You failed to register")
            return redirect(reverse('catalog'))
        else:
            return render(request, "accounts/register.html",{
                'form': form
            })
    else:
        register_form = UserRegistrationForm()
        return render(request, "accounts/register.html", {
            'form': register_form
        })