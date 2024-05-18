from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Booking, Menu
import json
from .forms import ApplicationForm, ModelForm, RegistrationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.db import IntegrityError
from django.core.paginator import Paginator, EmptyPage


# (FUNCTION-BASED)
def home(request):
    mydict = {}#used for any dynamic variables needed in template
    return render(request, 'welcome.html', mydict)

def about(request):
    about_content = {'about':"Based in Chicago, Illionois, Little Lemon is a restaurant that serves Italian, Greek and Mexican food."}
    return render(request, 'about_us.html', about_content)

@csrf_exempt
def menu(request):
    items = Menu.objects.select_related('category').all()
    category_name = request.GET.get('category')
    min_price = request.GET.get('min_price', 1)
    max_price = request.GET.get('max_price', 50)

    search = request.GET.get('search')
    ordering = request.GET.get('ordering')
    perpage = int(request.GET.get('perpage', 10))
    page = int(request.GET.get('page', 1))

    if category_name:
        items = items.filter(category__name=category_name)  #filter menu items by category
    if max_price:
        items = items.filter(price__lte=max_price)           #lte: <=
    if min_price:
        items = items.filter(price__gte=min_price)
    if search:
        items = items.filter(name__icontains=search)        #search
    if ordering:
        ordering_fields = ordering.split(",")
        items = items.order_by(*ordering_fields)

    
    
    paginator = Paginator(items, per_page=perpage)
    try:
        items = paginator.page(number=page)
    except EmptyPage:
        items = []

    context = {
        'menu_items': items,
        'min_price':min_price,
        'max_price':max_price,
        'perpage': perpage,
        'perpage_range': range(1, 11),  # Range for the per page dropdown (1 to 10)
    }
    return render(request, 'menu.html', context)
    
def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

def login_required_page(request):
    return HttpResponse("Login to make a reservation")

# (CLASS-BASED), can use mixins (multiple inheritence)
#common mixins: crud + list (warning, cant use together)
class Book(View):
    def get(self, request):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            # If not authenticated, redirect to the login page or a custom page
            return redirect(reverse('login'))
        # Retrieve booking data
        if request.user.is_staff:
            bookings = Booking.objects.all()
        else:
            bookings = Booking.objects.filter(name=request.user)

        #check formate parameter provided
        format = request.GET.get('format')
        if format == 'json':
            return JsonResponse({'bookings': list(bookings.values())})
        else:
            # Return booking data as HTML
            return render(request, 'reservations.html', {'bookings': bookings})

    def post(self, request):
        # Assuming booking information is in JSON format
        data = json.loads(request.body)

        name = data.get('name')
        date = data.get('date')
        time = data.get('time')

        # Create a new booking instance
        new_booking = Booking.objects.create(
            user=request.user,
            name=name,
            date=date,
            time=time
        )        
        try:
            new_booking.save()
        except IntegrityError:
            return JsonResponse({'error':'true','message':'required field missing'},status=400)
        
        return JsonResponse(model_to_dict(new_booking), status=201)

        

    

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