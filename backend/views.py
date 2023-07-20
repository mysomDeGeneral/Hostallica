from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from backend.models import Student, Hall, Room, Booking, HallManager
from django.template.defaulttags import register

# Create your views here.
@register.filter
def get_range(value):
    return range(1, value+1)




def index(request):
    students = Student.objects.all()
    return render(request, 'index.html')


def student_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'student_home.html')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')
    


def student_register(request):
    return render(request, 'student_register.html')


def student_home(request):
    students = Student.objects.all()
    halls = Hall.objects.all()
    return render(request, 'hallSelection.html', {'halls': halls,'students': students})
    


def student_booking(request,pk):
    hall = Hall.objects.get(id=pk)
    rooms = Room.objects.filter(hall=hall)
    return render(request, 'rooms.html', {'rooms': rooms, 'hall': hall})


def student_booking_history(request,pk):
    #return render(request, 'student_booking_history.html')
    hall = Hall.objects.all()
    room = Room.objects.get(id=pk)
    student = Student.objects.get(name=request.user)
    booking = Booking.objects.create(room=room, student=student)
    booking.save()
    return redirect('student_booking_history')



def hall_manager_home(request):
    return render(request, 'hall_manager_home.html')


def logout_user(request):
    logout(request)
    return redirect('login')



    