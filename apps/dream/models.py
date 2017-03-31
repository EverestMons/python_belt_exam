from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
     first_name = models.CharField(max_length=64)
     last_name = models.CharField(max_length=64)
     email = models.EmailField(unique=True)
     password = models.CharField(max_length=64)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

class Item(models.Model):
    name=models.CharField(max_length=64)
    user=models.ForeignKey(User, related_name='added_by')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Like(models.Model):
    user=models.ForeignKey(User, related_name='liked_items')
    item=models.ForeignKey(Item, related_name='wishers')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
