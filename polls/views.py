''' views model serves as a controller '''
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.core import serializers
from polls.models import Product, Image
from .forms import UploadFileForm

def homepage(request):
    ''' render homepage'''
    return render(request, 'polls/homepage.html')

def homepagejson(request):
    ''' send info to frontend'''
    category = request.GET.get('category')
    if category is None:
        queryset = Product.objects.all()
    else:
        queryset = Product.objects.filter(category=category)
    data = serializers.serialize("json", queryset)
    return HttpResponse(data, content_type='application/json')

def login(request):
    ''' render login/signup page'''
    return render(request, 'polls/login.html')

def about(request):
    ''' render about page'''
    return render(request, 'polls/about.html')

def auth_and_login(request, onsuccess='/polls/profile', onfail='/polls/login'):
    ''' login'''
    username = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return redirect(onsuccess)
    else:
        messages.add_message(request, messages.ERROR, 'Login Failed. Try again.', 'login', True)
        return redirect(onfail)

def logout(request):
    ''' logout and redirect'''
    if request.user.username:
        auth_logout(request)
        return render(request, 'polls/homepage.html')
    else:
        return redirect('/polls/login')

def auth_and_signup(request, onsuccess='/polls/profile', onfail='/polls/login'):
    ''' signup'''
    username = request.POST.get('email')
    password = request.POST.get('password')
    if not user_exists(username):
        user = User(username=username, email=username)
        user.set_password(password)
        user.save()
        auth_login(request, user)
        return redirect(onsuccess)
    else:
        messages.add_message(request, messages.INFO, 'User exists. Try again', 'signup', True)
        return redirect(onfail)

def user_exists(username):
    ''' check if user exists'''
    user_count = User.objects.filter(username=username).count()
    if user_count == 0:
        return False
    return True

def profile(request):
    ''' render profile page'''
    if request.user.username:
        user = User.objects.filter(username=request.user.username)
        context = {}
        context['user'] = user
        return render(request, "polls/profile.html", context)
    else:
        return redirect('/polls/login')

def profilejson(request):
    ''' send info to frontend'''
    if request.user.username:
        queryset = Product.objects.filter(username=request.user.username)
        data = serializers.serialize("json", queryset)
        return HttpResponse(data, content_type='application/json')
    else:
        return redirect('/polls/login')

def post(request):
    ''' post product'''
    if request.user.username and request.method == 'POST':
        MyImageForm = UploadFileForm(request.POST, request.FILES)
        name = request.POST.get('name')
        url = 'not upload'
        if MyImageForm.is_valid():
            picture = Image(name = name, pic = MyImageForm.cleaned_data["pic"])
            url = picture.getUrl()
            picture.addImage()
        price = request.POST.get('price')
        description = request.POST.get('description')
        category = request.POST.get('category')
        username = request.user.username

        if (Product.checkDuplicateProduct(name) == True):
            return redirect('/polls/profile')
               
        product = Product(name=name, username=username, price=price,\
                             description=description, category=category)
        if  url == 'not upload':
            product.url = '/media/index.png'
        else:
            product.url = str(url)
        product.addProduct()
        return redirect('/polls/profile')
    else:

        if request.user.username:
            return redirect('/polls/profile')
        else:
            return redirect('/polls/login')

def delete(request):
    ''' delete product'''
    if request.user.username and request.method == 'POST':
        name = request.POST.get('delete')
        user_name = request.user.username
        if name:
            product = Product.objects.get(name=name, username=user_name)
            if product is not None:
                product.deleteProduct()
        else:
            name = request.POST.get('name')
            price = request.POST.get('price')
            description = request.POST.get('description')
            product = Product.objects.get(name=name, username=user_name)
            if product is not None:
                product.updateProduct(price, description)
        return redirect('/polls/profile')
    else:
        if request.user.username:
            return redirect('/polls/profile')
        else:
            return redirect('/polls/login')
