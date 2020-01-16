from django.db import models
from django.contrib.auth.models import AbstractUser
<<<<<<< HEAD
from app1.models import foodpair
# Create your models here.

class CustomUser(AbstractUser):
    ucart = models.ForeignKey('cart', on_delete=models.CASCADE, null=True)


class cart(models.Model):
	
	foodp = models.ManyToManyField('app1.foodpair')
=======
# Create your models here.
class CustomUser(AbstractUser):
    pass

>>>>>>> 1300a0883187fc17cb3820d17245259c7535f431
