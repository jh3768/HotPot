from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.forms.models import model_to_dict
from django.core import serializers
#from polls.models import Product 
from polls.models import Product, Image
from .forms import UploadFileForm

def homepage(request):
    return render(request, 'polls/homepage.html')

def homepagejson(request):
    queryset = Product.objects.all()
    data = serializers.serialize("json", queryset)
    return HttpResponse(data, content_type='application/json')

def login(request):
    return render(request, 'polls/login.html')

def signup(request):
    return render(request, 'polls/signup.html')

def about(request):
    return render(request, 'polls/about.html')

def auth_and_login(request, onsuccess='/polls/profile', onfail='/polls/login'):
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
    if request.user.username:
        auth_logout(request)    
        return render(request, 'polls/homepage.html')
    else:
        return redirect('/polls/login')



def auth_and_signup(request, onsuccess='/polls/profile', onfail='/polls/login'):
    username = request.POST.get('email')
    password = request.POST.get('password')
    if not user_exists(username): 
        user = User(username=username, email=username)
        user.set_password(password)
        user.save()
        auth_login(request, user)
        return redirect(onsuccess)
    else:
        messages.add_message(request, messages.INFO, 'User already exists. Try again.', 'signup', True)
        return redirect(onfail) 

def user_exists(username):
    user_count = User.objects.filter(username=username).count()
    if user_count == 0:
        return False
    return True

def profile(request):
    if request.user.username:
        user = User.objects.filter(username=request.user.username)
        context = {}
        context['user'] =  user
        return render(request, "polls/profile.html", context)
    else:
        return redirect('/polls/login')

def profilejson(request):
    if request.user.username:
        queryset = Product.objects.filter(username=request.user.username)
        data = serializers.serialize("json", queryset)
        return HttpResponse(data, content_type='application/json')
    else:
        return redirect('/polls/login')

# def post(request):
#     if request.user.username and request.method == 'POST':
#         name = request.POST.get('name')
#         price = request.POST.get('price')
#         description = request.POST.get('description')
#         username = request.user.username
#         product = Product(name=name, username=username, price=price, description=description)
#         product.addProduct() 
#         return redirect('/polls/profile')
#     else:
#         if request.user.username:
#             return redirect('/polls/profile')
#         else:
#             return redirect('/polls/login')

def post(request):
    if request.user.username and request.method == 'POST':
        MyImageForm = UploadFileForm(request.POST, request.FILES)
        name = request.POST.get('name')
        print (name)
        if MyImageForm.is_valid():
            print ("yyyyyyyyyyyyyyyyyyyyyyyyyyyy")
            picture = Image(name = name, pic = MyImageForm.cleaned_data["image"])
            picture.addImage()
        price = request.POST.get('price')
        description = request.POST.get('description')
        username = request.user.username
        product = Product(name=name, username=username, price=price, description=description)
        product.addProduct() 
        return redirect('/polls/profile')
    else:
        if request.user.username:
            return redirect('/polls/profile')
        else:
            return redirect('/polls/login')  

def delete(request):
    if request.user.username and request.method == 'POST':
        name = request.POST.get('delete')
        if name:
            Product.deleteProduct(name, request.user.username)
        else:
            name = request.POST.get('name')
            price = request.POST.get('price')
            description = request.POST.get('description')
            Product.updateProduct(name, price, description)
        return redirect('/polls/profile')
    else:
        if request.user.username:
            return redirect('/polls/profile')
        else:
            return redirect('/polls/login')




