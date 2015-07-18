from django.shortcuts import render

from .models import Pizza

def index(request):
	pizzas = Pizza.objects.all().order_by('position')[:20]
	return render(request, 'banga/index.html', {'pizzas': pizzas})