from django.contrib import admin
from .models import Menu, MenuCategory, Booking, Logger, User, Person, Employee
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Menu)
admin.site.register(Booking)
admin.site.register(MenuCategory)
admin.site.register(Logger)
admin.site.register(Employee)

admin.site.unregister(User) 

@admin.register(User) 
class NewAdmin(UserAdmin): 
    readonly_fields = [ 
        'date_joined', 
    ] 
    def get_form(self, request, obj=None, **kwargs): 
        form = super().get_form(request, obj, **kwargs) 
        is_superuser = request.user.is_superuser 

        if not is_superuser: 
            form.base_fields['username'].disabled = True 

        return form 
    
@admin.register(Person) 
class PersonAdmin(admin.ModelAdmin): 
    list_display = ("last_name", "first_name") 
    search_fields = ("first_name__startswith", ) #custom search field