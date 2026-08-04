from django.db import models

# Create your models here.
class Cms(models.Model):
    image=models.ImageField(upload_to='images/', verbose_name='Image')
    title=models.CharField(max_length=60, verbose_name='Title')
    desc=models.TextField(max_length=100, verbose_name='Description')
    button=models.CharField(max_length=20, verbose_name='Button',blank=True, null=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'