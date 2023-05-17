from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login')
    else:
        return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url="login")
def home(request):

    context = {}
    return render(request, 'registration/index.html', context)

@login_required(login_url="login")
def depression(request):
    if request.method == 'POST':
        q1 = request.POST['question1']
        q2 = request.POST['question2']
        return redirect('prediction')
    context = {}
    return render(request, 'questions/depression.html', context)

@login_required(login_url="login")
def anxiety(request):
    if request.method == 'POST':
        q1 = request.POST['question1']
        q2 = request.POST['question2']
        return redirect('prediction')
    context = {}
    return render(request, 'questions/anxiety.html', context)


@login_required(login_url="login")
def stress(request):
    if request.method == 'POST':
        q1 = request.POST['question1']
        q2 = request.POST['question2']
        return redirect('prediction')
    context = {}
    return render(request, 'questions/stress.html', context)

@login_required(login_url="login")
def prediction(request):
    context = {}
    return render(request, 'prediction/prediction.html', context)
