from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm,CustomUserCreationForm
<<<<<<< HEAD
from .models import CustomUser, cart
=======
from .models import CustomUser
>>>>>>> 1300a0883187fc17cb3820d17245259c7535f431
# Register your models here.
class CustomAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','email']

<<<<<<< HEAD
admin.site.register(CustomUser,CustomAdmin)
admin.site.register(cart)
=======
admin.site.register(CustomUser,CustomAdmin)
>>>>>>> 1300a0883187fc17cb3820d17245259c7535f431
