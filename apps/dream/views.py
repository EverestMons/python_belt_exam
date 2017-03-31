from django.shortcuts import render,redirect, render, reverse
from django.contrib import messages
from .models import *
import re
from .models import *

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your views here.
def home(request):
    context = {
    'user_items': Item.objects.filter(wishers__user_id=request.session['id']),
    'other_items': Item.objects.exclude(wishers__user_id=request.session['id']),
    }
    return render(request, 'dream/home.html', context)

def login(request):
    return render(request, 'dream/login.html')

def processlogin(request):
    if request.method == 'POST':
        login_email = request.POST['login_email']
        login_pw = request.POST['login_pw']
        try:
            user = User.objects.get(email=login_email)
            request.session['first'] = user.first_name
            request.session['last'] = user.last_name
            request.session['email'] = user.email
            request.session['id'] = user.id
            if user.email:
                if user.password != login_pw:
                    messages.error(request, 'Invalid Password')
                    return redirect('wishlist:login')
                if user.password == login_pw:
                    return redirect('wishlist:home')
        except:
            messages.error(request, 'Hmm... we could not find any account by that name')
            return redirect('wishlist:login')
    else:
        return redirect('wishlist:login')

def register(request):
    return render(request, 'dream/register.html')

def processregister(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['register_email']
        password = request.POST['register_pw']
        password2 = request.POST['register_confpw']

        is_true=True

        if not firstname.isalpha():
            messages.error(request, 'First name can only be letters')
            is_true = False

        if not lastname.isalpha():
            messages.error(request, 'Last name can only be letters')
            is_true = False

        if len(firstname)< 2:
            messages.error(request, 'First name must be at least 3 characters')
            is_True=False

        if len(lastname)< 2:
            messages.error(request, 'Last name must be at least 3 characters')
            is_True=False

        if not email_regex.match(email):
            messages.error(request, 'Invalid Email')
            is_true = False

        if len(password) < 7:
            messages.error(request, 'Password must be at least 8 characters')
            is_true=False

        if not password == password2:
            messages.error(request, 'Passwords do not match' )
            is_true = False

        if is_true == False:
            return redirect('wishlist:register')

        if is_true:
            try:
                User.objects.get(email=email)
                if email:
                    messages.error(request, 'Email already in database' )
                    messages.error(request, 'User could not be created' )
                    return redirect('wishlist:register')
            except:
                user = User.objects.create(first_name=firstname, last_name=lastname, email=email, password=password)
                request.session['first'] = firstname
                request.session['last'] = lastname
                request.session['email'] = email
                request.session['id'] = user.id
                return redirect('wishlist:home')
    else:
        return redirect('wishlist:register')

def logout(request):
    request.session.clear()
    return redirect('wishlist:login')

def additem(request):
    return render(request, 'dream/additem.html')

def processitem(request):
    item_name=request.POST['item']
    if len(item_name) < 2:
        messages.error(request, 'Item name must be at least 3 characters')
        return redirect('wishlist:additem')
    else:
        Item.objects.create(name=item_name, user_id=request.session['id'])
        return redirect('wishlist:home')

def itempage(request, item_id):
    context = {
    'item': Item.objects.get(id=item_id),
    'users': Like.objects.filter(item_id=item_id)
    }
    return render(request, 'dream/itempage.html', context)


def addtolist(request, item_id):
    newitem = Like.objects.create(item_id=item_id, user_id=request.session['id'])
    return redirect('wishlist:home')

def removefromlist(request, item_id):
    newitem = Like.objects.filter(item_id=item_id, user_id=request.session['id']).delete()
    return redirect('wishlist:home')
