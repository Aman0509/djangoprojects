from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class NewUsers(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    phone_regex = RegexValidator(regex=r'^[0-9]+', message="Phone number should be of 10 digits")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    email = models.EmailField()


