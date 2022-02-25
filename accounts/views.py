from django.shortcuts import redirect, render
from accounts.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/home")
            except:
                pass
    else:
        form=RegisterForm()
    return render(response, "register.html", {"form":form})

def authlogin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        print(form.errors)
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"form":form})
def logout(request):
    auth_logout(request)
    return render(request,"login.html");
            