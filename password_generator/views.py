from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from .models import Contactus
from .models import Profile
from .models import Book
from django.contrib.auth.decorators import login_required
def password_generator(request):
    if request.method=="POST": 
        data=request.POST
        username=data.get('username')
        password=data.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid username')
            return redirect('/bro_html/')
        user=authenticate(username=username,password=password)
        request.session['name'] = username
        request.session.modified=True
        if user is None:
            messages.error(request,'Invalid password')
            return redirect('/bro_html/')
        else:
            return redirect('/next_page/')
    return render(request,"bro.html") 
def register_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, "Account already taken")    
        else:
            user = User.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
            )
            user.set_password(password)
            user.save()
            messages.info(request, 'Account successfully created')
            
    
    return render(request, 'register.html')
def next_page(request):
        return render(request, 'next.html')
def logout_page(request):
    logout(request)
    return redirect('/bro_html/')
def Home(requests):
    return render(requests,'home.html')
def book(request):
    if request.method == "POST":
        states = request.POST.get('state')
        chek_ins = request.POST.get('checkin')
        check_out = request.POST.get('checkout')
        adults = request.POST.get('adults')
        childrens = request.POST.get('children')
        phone_num = request.POST.get("phone")
        query = Book(
            state=states,
            check_out=check_out,
            check_in=chek_ins,
            Adults=adults,
            children=childrens,
            phone_no=phone_num
        )
        query.save()
        messages.info(request, "all set")
        return redirect('/book/')
    return render(request, 'book.html')
def profile(request): 
    print(request.session.get('name'))
    try:
        user=User.objects.get(username=request.session.get('name'))
        print(user)
        if request.method=="POST":
           data=request.POST
           username=data.get('username')
           query=Profile(user=username)
           query.save()
           messages.info(request,"Thank you reaching us we will back you soon")
           return redirect('/register_page/')    
    except Exception as e: 
        print('Exception : ' ,e)
    context={
        'user':user
    }
    return render(request,'profile.html',context)    
def contactus(request):
    if request.method=="POST":
        full_names=request.POST.get('full name')
        emails=request.POST.get('email')
        messagess=request.POST.get('message')
        query=Contactus(full_name=full_names,email=emails,message=messagess)
        query.save()
        messages.info(request,"Thank you reaching us we will back you soon")
        return redirect('/contactus/')
    return render(request,'contactus.html')   
def aboutus(requests):
    return render(requests,'aboutus.html')    