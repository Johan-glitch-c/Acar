from django.db import models

# Create your models here.


class OrderStatus(models.Model):
    status_name = models.CharField(max_length=100, verbose_name='Status Name')

    def __str__(self):
        return self.status_name


    class Meta:
        verbose_name = 'Order Status'
        verbose_name_plural = 'Order Statuses'


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now_add=True)
    order_name = models.CharField(max_length=100, verbose_name='Order Name')
    order_phone=models.CharField(max_length=20, verbose_name='Order Phone')
    order_status=models.ForeignKey(OrderStatus, on_delete=models.CASCADE, verbose_name='Order Status')


    def __str__(self):
        return self.order_name


    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


        