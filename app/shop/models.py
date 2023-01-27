from django.db import models

from account.models import Profile


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=90)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()

    def __str__(self):
        return f' Order #{self.id} item {self.item} buyer {self.profile}'