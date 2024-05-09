from django.db import models
from django.contrib.auth.models import User  # Example for a foreign key reference

class Booking(models.Model):
    # Unique ID (automatically created)
    id = models.AutoField(primary_key=True)

    # Customer who made the booking
    customer = models.ForeignKey(User, on_delete=models.CASCADE)  # Reference to User model

    # Details of the booking
    name = models.CharField(max_length=100)  # Name of the booking (e.g., customer name)
    date = models.DateField()  # Booking date
    time = models.TimeField()  # Booking time
    guests = models.IntegerField(default=1)  # Number of guests

    # Additional metadata
    created_at = models.DateTimeField(auto_now_add=True)  # When the booking was created
    updated_at = models.DateTimeField(auto_now=True)  # Last updated time

    def __str__(self):
        return f"Booking for {self.name} on {self.date} at {self.time}"

    class Meta:
        ordering = ['date', 'time']  # Default ordering

class MenuCategory(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=10)
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None, related_name="category_name")

    def __str__(self):
        return f"{self.name} : {self.category_id}"
        
class Logger(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    time_log = models.TimeField(help_text="dd/mm/yyyy")
    def __str__(self):
        return f"{self.first_name} {self.last_name} -- {self.time_log}"
    
class Person(models.Model): 
    last_name = models.TextField() 
    first_name = models.TextField() 

    def __str__(self): 
        return f"{self.last_name}, {self.first_name}" 

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    shift = models.IntegerField()

    def __str__(self):
        return self.first_name