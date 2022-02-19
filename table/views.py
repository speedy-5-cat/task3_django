from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import generic, View
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/table/accounts/login/')
def index(request):
    users = User.objects.all()
    return render(
        request,
        'mysite/index.html',
        {'users': users}
    )


def login(request):
    return render(
        request,
        'mysite/login.html'
    )


def register(request):
    return render(
        request,
        'mysite/register.html'
    )


class UserListView(generic.ListView):
    users = User.objects.all()
