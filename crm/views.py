from django.shortcuts import render,redirect
from .models import  Order, Cms, Service
from .forms import OrderForm
from telebot.sendmessage import sendTelegram
def index(request):
    images = Cms.objects.all().order_by('id')
    services = Service.objects.all()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()

            sendTelegram(order.order_name, str(order.order_phone), order.order_desc)

            return redirect('thanks')

    else:
        form = OrderForm()

    context = {'images': images,
               'services': services,
               'form':form}
    return render(request, 'index.html',context)





def thanks(request):
    return render(request, 'thanks.html')

def page_404(request, exception):
    return render(request, '404.html', status=404)