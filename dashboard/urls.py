from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.dashboard_redirect, name="redirect"),
    path("admin/", views.admin_dashboard, name="admin"),
    path("customer/", views.customer_dashboard, name="customer"),
]