from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from shop.models import Category,Products



def allcategories(request):
    c=Category.objects.all()
    return render(request,template_name='category.html',context={'c':c})





def product(request,p):
    c=Category.objects.get(name=p)
    p=Products.objects.filter(category=c)
    return render(request,template_name='product.html',context={'c':c,'p':p})

def detail(request,p):
    p=Products.objects.get(name=p)

    return render(request,template_name='detail.html',context={'p':p})

def user_login(request):
    if request.method=="POST":
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('shop:allcat')
        else:
            return HttpResponse('invalid credentials')
    return render(request,template_name='login.html')


def register(request):
    if request.method=="POST":
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        f=request.POST['f']
        l=request.POST['l']
        e=request.POST['e']
        if p==cp:
            u=User.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e)
            return redirect('shop:allcat')
        else:
            return HttpResponse('passwords do not match')

    return render(request,template_name='register.html')
@login_required
def user_logout(request):
    logout(request)
    return redirect('shop:login')

