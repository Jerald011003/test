from django.db import models
from django.urls import reverse

from django.db.models.signals import pre_save
from products.models import Product
# Create your models here.


class ProductTag(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.title

def tag_pre_save_receiver(sender, intance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(intance)

pre_save.connect(tag_pre_save_receiver, sender=ProductTag)