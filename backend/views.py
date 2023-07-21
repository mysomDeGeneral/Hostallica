from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout 
from backend.models import Student, Hall, Room, Booking, HallManager
from django.template.defaulttags import register
from django.conf import settings
import stripe
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, View

stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.
@register.filter
def get_range(value):
    return range(1, value+1)




def index(request):
    students = Student.objects.all()
    return render(request, 'index.html')


def _login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next', settings.LOGIN_REDIRECT_URL))
    else:
        return render(request, 'login.html')
    


def student_register(request):
    return render(request, 'student_register.html')


def _hall(request):
    #students = Student.objects.all()
    halls = Hall.objects.all()
    return render(request, 'hallSelection.html', {'halls': halls})
    


def _rooms(request,pk):
    hall = Hall.objects.get(id=pk)
    rooms = Room.objects.filter(hall=hall)
    return render(request, 'rooms.html', {'rooms': rooms, 'hall': hall})


def _booking(request,room_id):
    #return render(request, 'student_booking_history.html')
    #hall = Hall.objects.all()
    key = settings.STRIPE_PUBLISHABLE_KEY
    room = get_object_or_404(Room, id=room_id)
    hall = Hall.objects.get(name=room.hall)
    student = Student.objects.get(name=request.user.name)
    booking = Booking.objects.create(room=room, student=student, hall=hall)
    booking.save()
    return render(request, 'confirmation.html', {'booking': booking, 'key': key} )



def hall_manager_home(request):
    return render(request, 'hall_manager_home.html')


def logout_user(request):
    logout(request)
    return redirect('login')

def _confirmation(request):
    booking = Booking.objects.all()
    return render(request, 'confirmation.html')


#stripe
def charge(request):
    if request.method == 'POST':
        student = Student.objects.get(name=request.user.name)
        booking = Booking.objects.get(student=student)
        amount = booking.room.price
        charge = stripe.Charge.create(
            amount=amount,
            currency='usd',
            description='Payment Gateway',
            source=request.POST['stripeToken']
        )
        return redirect('success')
    return render(request, 'confirmation.html')

