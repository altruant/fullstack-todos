from django.db import models
from django.utils import timezone
# Create your models here.
class Item(models.Model):
    text = models.CharField(max_length=80)
    checked = models.BooleanField(default=False)
    due_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
