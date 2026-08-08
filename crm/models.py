from django.db import models

# Create your models here.




class Order(models.Model):
    order_dt = models.DateTimeField(auto_now_add=True)
    order_name = models.CharField(max_length=100, verbose_name='Order Name')
    order_phone=models.CharField(max_length=20, verbose_name='Order Phone')
    order_desc=models.TextField(max_length=200, verbose_name='Order Description', blank=True, null=True)

    def __str__(self):
        return self.order_name


    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class Cms(models.Model):
    image=models.ImageField(max_length=200, upload_to='images/', verbose_name='Image')
    title=models.CharField(max_length=60, verbose_name='Title')
    desc=models.TextField(max_length=100, verbose_name='Description')
    button=models.CharField(max_length=20, verbose_name='Button',blank=True, null=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'



class Service(models.Model):
    title=models.CharField(max_length=60, verbose_name='Title')
    desc=models.TextField(max_length=200, verbose_name='Description')
    image=models.ImageField(upload_to='service_images/', verbose_name='Image')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'