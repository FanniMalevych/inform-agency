from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from accounts.forms import LoginForm


def login(request: HttpRequest) -> HttpResponse:
    form = LoginForm()
    if request.method == "POST":
        uname = request.POST.get("username")
        upass = request.POST.get("password")
        user = authenticate(username=uname, password=upass)
        if user is not None:
            auth_login(request, user)
            return redirect("agency:index")
    else:
        if request.user.is_authenticated:
            return redirect("agency:index")
        else:
            return render(request, "registration/login.html", {"form": form})
