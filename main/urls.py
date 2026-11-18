from django.urls import path
from django.http import HttpResponse

app_name = "main"


def home(request):
    return HttpResponse("Welcome to LutoLuto!")


urlpatterns = [
    path("", home, name="home"),
]