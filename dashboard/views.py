from functools import wraps

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from users.models import User


def role_required(required_role):

    def decorator(view_func):

        @wraps(view_func)
        @login_required
        def wrapper(request, *args, **kwargs):

            if request.user.role != required_role:
                raise PermissionDenied

            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator


@login_required
def dashboard_redirect(request):

    if request.user.role == User.Role.ADMIN:
        return redirect("dashboard:admin")

    return redirect("dashboard:customer")


@role_required('admin')
def admin_dashboard(request):

    return render(
        request,
        "dashboard/admin_dashboard.html"
    )


@role_required('customer')
def customer_dashboard(request):

    return render(
        request,
        "dashboard/customer_dashboard.html"
    )