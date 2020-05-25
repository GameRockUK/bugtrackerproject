from django.db import models
from django.contrib.auth.models import User

# Create your models here.

COUNTRY_CHOICES = (
    ('united kingdom','UNITED KINGDOM'),
    ('united states', 'UNITED STATES'),
    ('ireland','IRELAND'),
    ('france','FRANCE'),
    ('australia','AUSTRALIA'),
)

class contactform(models.Model):
    full_name = models.CharField(max_length=40, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, choices=COUNTRY_CHOICES, blank=False)
    email = models.EmailField(max_length=254, default='test@test.com')
    description = models.CharField(max_length=500, blank=False)
    budget = models.IntegerField(blank=False)
