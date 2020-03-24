
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import hotels,units,reviews,books,orders,user_information
from django.utils.crypto import get_random_string
from django.db.models import Sum
from datetime import datetime
from django.contrib import messages


def login_user(request):
    if request.method == "GET":
        return render(request , "booking/login.html")
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request,user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "booking/login.html", {"message": "Invalid credentials."})

def register_user(request):
    if request.method == "GET":
        return render(request , "booking/register.html")
    username = request.POST["username"]
    password = request.POST["password"]
    firstname = request.POST["firstname"]
    lastname = request.POST["lastname"]
    email = request.POST["email"]
    newuser = User.objects.create_user(username, email, password)
    newuser.first_name = firstname
    newuser.last_name = lastname
    newuser.save()
    #to add additional information about user
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request,user)
        newuser = user_information()
        newuser.user_id = request.user
        #to generate order number when new user is register
        newuser.orderNumber = get_random_string(length=8)
        newuser.save()
        return HttpResponseRedirect(reverse("index"))
    return render(request, "booking/login.html")
    

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def index(request):
    if request.method == "GET":
        context = {
                "hotels" : hotels.objects.all(),
            }
        return render(request, "booking/index.html", context)
    return HttpResponseRedirect(reverse("hotel"))

def hotel(request, hotels_id):
    if request.method == "GET":
        context = {
            "hotel" : hotels.objects.get(id = hotels_id),
            "units" : units.objects.filter(hotel_id = hotels_id),
            "reviews" : reviews.objects.filter(hotel_id = hotels_id)
        }
        return render(request, "booking/hotel.html", context)
    if request.method == "POST":
        #to make sure that the user was login
        if request.user.is_authenticated:
            newreview = reviews()
            newreview.user_id = request.user
            newreview.hotel_id = hotels.objects.get(id = hotels_id)
            newreview.comment = request.POST["comment"]
            newreview.rate = request.POST["rate"]
            newreview.save()
            context = {
                "hotel" : hotels.objects.get(id = hotels_id),
                "units" : units.objects.filter(hotel_id = hotels_id),
                "reviews" : reviews.objects.filter(hotel_id = hotels_id)
            }
            return render(request, "booking/hotel.html", context)
        else:
            return HttpResponseRedirect(reverse("login")) 


def book(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            unit_id = int(request.POST["room_id"])
            unit_details = units.objects.get(id = unit_id)
            newbook = books()
            newbook.user_id = request.user
            newbook.unit_id = unit_details
            newbook.from_date = request.POST["from"]
            newbook.to_date = request.POST["to"]
            date_format = "%Y-%m-%d"
            a = datetime.strptime(str(request.POST["from"]), date_format)
            b = datetime.strptime(str(request.POST["to"]), date_format)
            newbook.num_of_days = (b - a).days
            newbook.price_per_unit =  newbook.num_of_days * unit_details.price
            newbook.order_num = user_information.objects.get(user_id = request.user).orderNumber
            print(newbook)
            newbook.save()
            return HttpResponse('')
    else:
        return HttpResponseRedirect(reverse("login"))


def cart(request):
    if request.method == "GET":
        sum = books.objects.filter(user_id = request.user).filter(is_paid = False).aggregate(Sum('price_per_unit'))
        summ = sum['price_per_unit__sum']
        context = {
            "books" : books.objects.filter(user_id = request.user , is_paid = False),
            "summ" : summ
        }
        return render(request, "booking/cart.html", context)
    if request.method == "POST":
        neworder = orders()
        neworder.user_id = request.user
        neworder.order_number = user_information.objects.get(user_id = request.user).orderNumber
        sum = books.objects.filter(user_id = request.user).filter(is_paid = False).aggregate(Sum('price_per_unit'))
        summ = sum['price_per_unit__sum']
        neworder.total_price = summ
        neworder.is_paid = True
        neworder.save()
        #to make all books paid when confirm the order
        items = books.objects.filter(user_id = request.user , is_paid = False)
        for item in items:
            item.is_paid = True
            item.save()
        #to change order number when you finish the order
        new = user_information.objects.get(user_id = request.user)
        new.orderNumber = get_random_string(length=8)
        new.save()
        return HttpResponseRedirect(reverse("history"))

def delete(request,books_id):
    record = books.objects.get(id = books_id)
    record.delete()
    return HttpResponseRedirect(reverse("cart"))


def history(request):
    if request.method == "GET":
        context = {
            "orders" : orders.objects.filter(user_id = request.user)
        }
        return render(request, "booking/history.html", context)  
    if request.method == "POST":
        context = {
            "orders" : orders.objects.filter(user_id = request.user)
        }
        return render(request, "booking/history.html", context)