# encoding=utf-8

from django.db import models
import os

class Pizza(models.Model):
    name  = models.CharField(max_length=30, verbose_name='שם')
    description = models.TextField(verbose_name='תיאור')
    dough = models.ForeignKey('Dough', verbose_name='בצק')
    toppings = models.ManyToManyField('Topping', verbose_name='תוספות')
    position = models.IntegerField(verbose_name='מיקום')

    class Meta:
        verbose_name = 'פיצה'
        verbose_name_plural = 'פיצות'
        # unique_together = (("dough", "toppings"),)

    def __unicode__(self):
        return self.name

    def get_first_image(self):
        if self.images.filter(main=True):
            return "/media/{0}/{1}".format(self.name, self.images.filter(main=True)[0])
        return "" #todo: placeholder

    def get_toppings(self):
        return ", ".join([t.name for t in self.toppings.all()])

def img_uploader(instance, filename):
    return u"{0}/{1}".format( instance.pizza.name, filename )

class PizzaImage(models.Model):
    image = models.ImageField(upload_to=img_uploader, verbose_name='תמונה')
    pizza = models.ForeignKey(Pizza, verbose_name='פיצה', related_name='images')
    main  = models.BooleanField(verbose_name='עיקרי')

    class Meta:
        verbose_name = 'תמונה לפיצה'
        verbose_name_plural = 'תמונות לפיצה'

    def __unicode__(self):
        return os.path.basename(self.image.name)

class Dough(models.Model):
    name = models.CharField(max_length=30, verbose_name='שם')

    class Meta:
        verbose_name = 'בצק'
        verbose_name_plural = 'בצקים'

    def __unicode__(self):
        return self.name

class Topping(models.Model):
    name = models.CharField(max_length=30, verbose_name='שם')

    class Meta:
        verbose_name = 'תוספת'
        verbose_name_plural = 'תוספות'

    def __unicode__(self):
        return self.name




# python manage.py loadtestdata banga.PizzaImage:50 banga.Dough:50 banga.Topping:50 banga.Pizza:50