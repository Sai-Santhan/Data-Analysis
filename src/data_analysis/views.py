from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect


def logout_view(request):
    logout(request)
    return redirect("login")


def login_view(request):
    if request.user.is_authenticated:
        return redirect('sales:home')
    else:
        error_message = None
        form = AuthenticationForm()
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    if request.GET.get('next'):
                        return redirect(request.GET.get("next"))
                    else:
                        return redirect("sales:home")
            else:
                error_message = "Oops ... Something went Wrong!"
        context = {
            "form": form,
            "error_message": error_message
        }

        return render(request, "auth/login.html", context)


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('sales:home')
    else:
        error_message = None
        form = UserCreationForm()
        if request.method == "POST":
            form = UserCreationForm(data=request.POST)
            if form.is_valid():
                form.save()
                # login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get("next"))
                else:
                    return redirect("sales:home")
            else:
                error_message = "Oops ... Something went Wrong!"
        context = {
            "form": form,
            "error_message": error_message
        }
        return render(request, "auth/signup.html", context)
