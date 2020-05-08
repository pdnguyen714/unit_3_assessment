from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from .models import Item

# Create your views here.

def items_index(request):
    items = Item.objects.all()
    return render(request, 'index.html', { 'items': items })

class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    success_url = '/'

class ItemDelete(DeleteView):
    model = Item
    success_url = '/'