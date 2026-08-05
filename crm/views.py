from django.shortcuts import render,redirect
from .models import  Order, Cms, Service
from .forms import OrderForm
def index(request):
    images = Cms.objects.all()
    sevices = Service.objects.all()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')

    else:
        form = OrderForm()

    context = {'images': images,
               'services': sevices,
               'form':form}
    return render(request, 'index.html',context)





def thanks(request):
    return render(request, 'thanks.html')