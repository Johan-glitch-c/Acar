from django.db import models

# Create your models here.
class TeleBotSettings(models.Model):
    token = models.CharField(max_length=255)
    chat_id = models.CharField(max_length=255)
    message = models.TextField(verbose_name="Message")
    def __str__(self):
        return self.chat_id


    class Meta:
        verbose_name = "TeleBot Setting"
        verbose_name_plural = "TeleBot Settings"