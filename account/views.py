from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse("Login successfully")
                else:
                    return HttpResponse("Disabled account")
            else:
                return HttpResponse("Invalid login details")
    else:
        form = LoginForm()
    return render(request,'account/login.html',{'form':form})


@login_required
def dashboard(request):
    return render(
        request,
        'account/dashboard.html',
        {
            'section': 'dashboard',
        }
    )
                  