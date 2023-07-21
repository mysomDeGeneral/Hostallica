from django.db import models
from backend.models import Room 

# Create your models here.
class Payment(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100)
    price = models.IntegerField()
    
    def get_display_price(self):
        return "{:.2f}".format(self.price / 100)