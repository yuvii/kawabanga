# encoding=utf-8

from django.contrib import admin
from .models import Pizza, PizzaImage, Dough, Topping

# class ToppingInline(admin.TabularInline):
# 	model = Topping
# 	extra = 3

class PizzaImageInline(admin.TabularInline):
	model = PizzaImage
	extra = 3

class PizzaAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'dough', 'get_toppings')
	order_by = ('position',)

	def get_toppings(self, x):
		return ', '.join( [t.name for t in x.toppings.all() ] )
	get_toppings.short_description = u'תוספות'

	inlines = [PizzaImageInline]



admin.site.register(Dough)
admin.site.register(Topping)
admin.site.register(Pizza, PizzaAdmin)