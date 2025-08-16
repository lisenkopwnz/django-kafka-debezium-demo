from django.db import models

class DataEvent(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField()
    is_valid = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} (Value: {self.value})"
    