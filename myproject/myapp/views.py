from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Booking
import json
from .forms import ApplicationForm, ModelForm
from myapp.models import Logger

# (FUNCTION-BASED)
def home(request):
    # form = ApplicationForm() 
        return render(request, 'welcome.html')#, {'form': form}) 

def about(request):
    return HttpResponse("About us")

def menu(request):
    return HttpResponse("Menu for Little Lemon")

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
