from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout 
from backend.models import Student, Hall, Room, Booking, HallManager
from django.template.defaulttags import register
from django.conf import settings
import stripe
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.
@register.filter
def get_range(value):
    return range(1, value+1)




def index(request):
    return render(request, 'index.html')


#@login_required
def _login(request):
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not username or not password:
            messages.error(request, 'Please enter both username and password')
            return render(request, 'login.html')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', settings.LOGIN_REDIRECT_URL)
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html', {'username': username})
    else:
        return render(request, 'login.html')
    


def student_register(request):
    return render(request, 'student_register.html')


def _hall(request):
    #students = Student.objects.all()
    halls = Hall.objects.all()
    return render(request, 'hallSelection.html', {'halls': halls})
    

@login_required
def _rooms(request,pk):
    hall = get_object_or_404(Hall,id=pk)
    rooms = Room.objects.filter(hall=hall)
    return render(request, 'rooms.html', {'rooms': rooms, 'hall': hall})


@login_required
def _booking(request,room_id):
    key = settings.STRIPE_PUBLISHABLE_KEY
    bookings = Booking.objects.all()
    students = Student.objects.all()
    room = get_object_or_404(Room, id=room_id)
    student = get_object_or_404(Student,name=request.user.name)
    hall = get_object_or_404(Hall,name=room.hall)
    #variable to check if booking exists
    booking_exists = False

    #check if booking exists
    for item in bookings:
        if item.student == student:
            booking_exists = True
            break
            return redirect('booking_details')
    if not booking_exists:   
        #create booking
        booking = Booking.objects.create(room=room, student=student, hall=hall)
        booking.save()
        student.room = room
        student.save()
    return redirect('booking_details')



def hall_manager_home(request):
    return render(request, 'hall_manager_home.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('index')

def _confirmation(request):
    booking = Booking.objects.all()
    return render(request, 'confirmation.html')


#stripe
@login_required
def charge(request):
    
        student = get_object_or_404(Student,name=request.user.name)
        booking = get_object_or_404(Booking,student=student)
        amount = booking.room.price

        #update booking status
        booking.paid = True
        booking.save()

        #create stripe charge
        charge = stripe.Charge.create(
            amount=amount,
            currency='usd',
            description='Payment Gateway',
            source=request.POST['stripeToken']
        )
        return redirect('booking_details')



@login_required
def _booking_details(request):
    key = settings.STRIPE_PUBLISHABLE_KEY
    room = get_object_or_404(Room,id=request.user.room.id)
    students = Student.objects.filter(room=room)
    booking = get_object_or_404(Booking,student=request.user.id)
    bookings = Booking.objects.all()
    return render(request, 'booking.html', {'booking':booking,'bookings': bookings, 'key': key, 'students': students, 'room': room})


    
@login_required
def _cancel_booking(request):
    booking = get_object_or_404(Booking,student=request.user.id)
    print(booking)
    booking.delete()
    return redirect('index')






#test view
def test(request):
    return render(request, 'hallSelection.html')



