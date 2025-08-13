from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, logout

# Create your views here.
def register(request):

    form = RegisterForm() 
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')

    return render(request, 'register.html', context={"form":form})

def login_page(request):

    form = LoginForm() 
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('task_list')

    return render(request, 'login.html', context={"form":form})

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')

