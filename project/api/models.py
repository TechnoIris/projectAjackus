from django.db import models
from django.db.models import CharField, IntegerField, TextField
from django.core.validators import validate_email
from django.core.validators import RegexValidator

import re
from django.urls import reverse

# Create your models here.

def validate_password(key):
    try:
        if len(key)>7:
            if bool(re.findall('[A-Z]+', key)) and bool(re.findall('[a-z]+', key)):
                return key
            else:
                raise ValidationError('number format not acceptable. validlength accuracy: 10')
    except:
        raise ValueError

class Author(models.Model):
    email = models.EmailField(primary_key=True, max_length=254, blank=False, unique=True, validators=[validate_email])
    password = models.CharField(max_length=254, blank=False, unique=False, validators=[validate_password])
    fullName = CharField(max_length=254, blank=False, unique=False)
    phone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10,10}$')])
    address = models.TextField(max_length=254, blank=True)
    city = models.CharField(max_length=254, blank=True)
    state = models.CharField(max_length=254, blank=True)
    country = models.CharField(max_length=254, blank=True)
    pincode = models.CharField(max_length=6, validators=[RegexValidator(r'^\d{1,6}$')])

    def __str__(self):
        return self.fullName

    #on submit click on the register, it redirects to url below
    def registerAuthor(self):
        return reverse('api:index')

class Contitem(models.Model):
    title = models.CharField(max_length=30, blank=False)
    body = models.TextField(max_length=300, blank=False)
    summary = models.TextField(max_length=60, blank=False)
    pdf = models.FileField(blank=False, upload_to='pdf/')

    def __str__(self):
        return f"{self.title}"

class Admin(models.Model):
    username = models.CharField(primary_key=True, max_length=254, blank=False, unique=True)
    password = models.CharField(max_length=254, blank=False, validators=[validate_email])
