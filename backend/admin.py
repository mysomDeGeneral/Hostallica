from django.contrib import admin
from backend.models import Student, Hall, Room, Booking, HallManager
from .forms import StudentCreationForm
# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_number','type','floor','hall',]

class HallAdmin(admin.ModelAdmin):
    list_display = ['name','capacity','floors',]

class BookingAdmin(admin.ModelAdmin):
    list_display = ['student','room','date','start_time','end_time',]



class StudentAdmin(admin.ModelAdmin):
    form = StudentCreationForm
    model = Student
    list_display = ['name','username','phone','program',]

admin.site.register(HallManager)

custom_models = [Student,Hall, Room, Booking]
custom_models_admin = [StudentAdmin, HallAdmin, RoomAdmin, BookingAdmin]

for model, model_admin in zip(custom_models, custom_models_admin):
    admin.site.register(model, model_admin)