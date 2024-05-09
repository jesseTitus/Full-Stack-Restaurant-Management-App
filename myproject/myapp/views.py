from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Booking, Menu
import json
from .forms import ApplicationForm, ModelForm, RegistrationForm
from django.contrib.auth import login
from myapp.models import Logger

# (FUNCTION-BASED)
def home(request):
    mydict = {}#used for any dynamic variables needed in template
    return render(request, 'welcome.html', mydict)

def about(request):
    about_content = {'about':"Based in Chicago, Illionois, Little Lemon is a restaurant that serves Italian, Greek and Mexican food."}
    return render(request, 'about_us.html', about_content)

def menu(request):
    menu_items = Menu.objects.all()
    context = {
        'menu_items': menu_items,
    }
    return render(request, 'menu.html', context)

# def book(request):
    # if request.method == 'GET':
    #     return HttpResponse("Make a booking")

# (CLASS-BASED), can use mixins (multiple inheritence)
#common mixins: crud + list (warning, cant use together)
class Book(View):
    def get(self, request):
        # Retrieve booking data
        bookings = Booking.objects.all()  # Get all bookings

        # Convert booking data to JSON-friendly format
        booking_data = [
            {
                'id': booking.id,
                'name': booking.name,
                'date': booking.date,
                'time': booking.time,
            }
            for booking in bookings
        ]

        # Return booking data as JSON
        return JsonResponse({'bookings': booking_data})

    def post(self, request):
        # Assuming booking information is in JSON format
        data = json.loads(request.body)

        # Create a new booking
        new_booking = Booking(
            name=data['name'],
            date=data['date'],
            time=data['time'],
        )
        new_booking.save()

        return JsonResponse({
            'message': 'Booking created successfully',
            'booking_id': new_booking.id,
        })
    

# FORMS -- 
def form(request): 
    if request.method == 'POST': 
        form = ApplicationForm(request.POST) 
        # check whether it's valid: 
        if form.is_valid(): 
            # process the data  
            # ... 
            # ... 
            return HttpResponse('Form successfully submitted') 
    else:
        form = ApplicationForm() 
        return render(request, 'form.html', {'form': form}) 

def modelform(request):
    if request.method == 'POST':
        form = ModelForm(request.POST)    #update form object with contents of POST inside request object
        if form.is_valid():
            form.save()
            return HttpResponse('form submitted successfully')
        else:
            return HttpResponse('invalid form')
    else:
        form = ModelForm()
        context = {"form": form}
        return render(request, "form.html", context)
    

#-------------ACCOUNT RELATED VIEWS------------
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('home')  # Redirect to the home page or another page
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})  # Render the registration form