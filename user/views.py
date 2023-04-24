from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm


from django.template.loader import get_template
from django.template import Context



def index(request):
    return render(request, 'user/index.html', {'title': 'index'})



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, f'Hesabınız başarıyla oluşturuldu.şimdi giriş yapabilirsiniz.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title': 'buradan kayıt ol'})
    messages.info(request, f"hata")


def Login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' Hoşgeldiniz {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'üzgünüz girişiniz hatalı')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form, 'title': 'log in'})