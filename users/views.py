from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm, ProfileForm


def register_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard:redirect")

    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(
                request,
                "Welcome to LutoLuto! Account created successfully."
            )

            return redirect("dashboard:redirect")

    else:
        form = RegistrationForm()

    return render(
        request,
        "users/register.html",
        {"form": form}
    )


def login_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard:redirect")

    if request.method == "POST":
        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():
            login(request, form.get_user())

            return redirect("dashboard:redirect")

        messages.error(
            request,
            "Invalid username or password."
        )

    else:
        form = AuthenticationForm()

    return render(
        request,
        "users/login.html",
        {"form": form}
    )


@login_required
def logout_view(request):

    if request.method == "POST":
        logout(request)

        messages.success(
            request,
            "You have logged out successfully."
        )

        return redirect("users:login")

    return redirect("dashboard:redirect")


@login_required
def profile_view(request):
    return render(request, "users/profile.html")


@login_required
def edit_profile_view(request):

    if request.method == "POST":
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=request.user
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Profile updated successfully."
            )

            return redirect("users:profile")

    else:
        form = ProfileForm(instance=request.user)

    return render(
        request,
        "users/edit_profile.html",
        {"form": form}
    )