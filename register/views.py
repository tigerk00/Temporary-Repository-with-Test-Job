from django.shortcuts import render, redirect
from .forms  import RegisterForm
from django.contrib import messages
from django.contrib.auth import logout



def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            logout(request)
            return redirect("login")
        else:
            messages.error(request, f"Ошибка, перепроверьте вводимые данные.")
            form = RegisterForm()

    form = RegisterForm()
    return render(request, "register/register.html", {"form":form,})