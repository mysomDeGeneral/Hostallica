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
    room_type = (("Flat","Flat"),("Four in Room","Four in Room"))
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    room_number = models.PositiveIntegerField()
    type = models.CharField(choices=room_type, max_length=20, default='Four in Room')
    floor = models.PositiveIntegerField()
    price = models.PositiveIntegerField(default=1200)

    def __str__(self):
        return str(self.room_number)
    
    

class Booking(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE,null=True)
    date = models.DateField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    

    def __str__(self):
        return str(self.student) + " " + str(self.room) + " " + str(self.date) + " " + str(self.start_time) + " " + str(self.end_time)


        return str(self.student) + " " + str(self.room) + " " + str(self.date) + " " + str(self.hall)
    


class HallManager(models.Model):
    first_name = models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    manager_ID = models.CharField(max_length=50)
    manager_contact = models.CharField(max_length=100)
    manager_email = models.EmailField(max_length=100)
    position = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    hall = models.ForeignKey(Hall, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Hall Manager: {self.first_name} {self.last_name} {self.manager_contact} {self.position}'