from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from users.forms import UserLoginForm,UserRegistrationForm,UserProfileForm
from django.contrib.auth.decorators import login_required

from django.contrib import auth,messages
from products.models import Basket


# Create your views here.
#настройка переадресации на профиль с анонимной странички @login_required

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm
    context = {'form': form}
    return render(request, 'users/login.html', context)


def register(request):
    if request.method =='POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Вы успешно зарегестрировались')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form':form}
    return render(request, 'users/register.html',context)

def profile(request):
    if request.method =='POST':
        form = UserProfileForm(data=request.POST,files=request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form =UserProfileForm(instance=request.user)
    baskets = Basket.objects.filter(user=request.user)
    total_quantity = 0
    total_sum = 0
    for basket in baskets:
        total_quantity += basket.quantity
        total_sum += basket.sum()
    context = {'form':form,
               'baskets': baskets,
               'total_quantity': total_quantity,
               'total_sum': total_sum
               }
    return render(request,'users/profile.html',context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))