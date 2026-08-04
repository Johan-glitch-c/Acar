from django.shortcuts import render
from .models import OrderStatus, Order, Cms

def index(request):
    images = Cms.objects.all()
    context = {'images': images}
    return render(request, 'index.html',context)