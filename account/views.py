from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout


# Create your views here.

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("list")
            

    else:
        form = AuthenticationForm()
        return render(request, "account.html", {"form":form})

def logout_view(request):
    logout(request)
    return redirect("list")
