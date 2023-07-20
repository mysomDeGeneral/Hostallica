from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
class Student(AbstractUser):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='profile/', null=True, blank=True)
    hall = models.ForeignKey('Hall', on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    

class Hall(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    floors = models.IntegerField()
    picture = models.ImageField(upload_to='hall/', null=True, blank=True) 

    def __str__(self):
        return self.name


class Room(models.Model):
    room_type = (("One in Room","One in Room"),("Two in Room","Two in Room"),("Three in Room","Three in Room"),("Four in Room","Four in Room"))
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    room_number = models.IntegerField()
    type = models.CharField(choices=room_type, max_length=20, default=1)
    floor = models.PositiveIntegerField(choices=[], blank=True)

    def __str__(self):
        return str(self.room_number)
    
    def save(self, *args, **kwargs):
        self.floor = self.hall.floors
        super().save(*args, **kwargs)
    

class Booking(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)

    def __str__(self):
        return str(self.student) + " " + str(self.room) + " " + str(self.date) + " " + str(self.start_time) + " " + str(self.end_time)
    

class HallManager(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    hall = models.ForeignKey(Hall, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name