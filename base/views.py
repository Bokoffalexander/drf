from django.shortcuts import render
# Create your views here.
from .models import Item

def all(request):
    
    items = Item.objects.order_by('created')
    
    return render(request, 'items.html', {'items':items})

