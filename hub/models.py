from django.db import models
from django.contrib.auth.models import User


class Icon(models.Model):
    image = models.ImageField(upload_to='.')

    def __unicode__(self):
        return self.image.name


class Item(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField()
    quantity = models.IntegerField()
    icon = models.ForeignKey(Icon)

    class Meta:
        unique_together = ("name", "character")

    def __unicode__(self):
        return self.name


class Slot(models.Model):
    name = models.CharField(max_length=75)
    items = models.ManyToManyField(Item)

    def __unicode__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=75, unique=True)
    owner = models.ForeignKey(User)
    slots = models.ManyToManyField(Slot)

    def __unicode__(self):
        return self.name
