from random import choices
from sre_constants import CATEGORY
from django.db import models
from django.urls import reverse
from PIL import Image


class Firm(models.Model):
    firm = models.CharField(max_length=30, help_text="Enter name of manufacturer")

    def __str__(self):
        return self.firm


class Product(models.Model):
    BASE = 'base'
    TOP = 'top'
    GEL = 'gel'
    GEL_LACK = 'gel-lack'

    CATEGORY = {
        (BASE, 'base'),
        (TOP , 'top'),
        (GEL, 'gel'),
        (GEL_LACK, 'gel-lack'),
    }

    name = models.CharField(max_length=100)
    firm = models.ForeignKey('Firm',on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=100, null=True, choices=CATEGORY)
    volume = models.IntegerField()
    amount = models.IntegerField(default=0)
    description = models.TextField(help_text = "Enter short product deskription")
    colour = models.CharField(max_length=30)
    price = models.FloatField()
    image = models.ImageField(default='no_image.jpg', upload_to='pictures/product_image')

    def __str__(self):
        return self.name

    def get_product_url(self):
        return reverse('view', args=[str(self.id)])

    def get_buy_url(self):
        return reverse('buy', args=[str(self.id)])   

 
