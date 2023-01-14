from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    context = {'form':form}
    return render(request, 'users/register.html', context)


@login_required(login_url='login')
def profile(request):
    context = {}
    return render(request, 'users/profile.html', context)
