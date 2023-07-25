from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout 
from backend.models import Student, Hall, Room, Booking, HallManager, Message, HallImage
from django.template.defaulttags import register
from django.conf import settings
import stripe
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest




stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.
@register.filter
def get_range(value):
    return range(1, value+1)

@register.filter
def first_image(hall, images):
    for image in images:
        if image.hall == hall:
            return image
    return None




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
    
    


def _authenticate(request):
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not username or not password:
            messages.error(request, 'Please enter both username and password')
            return render(request, 'authenticate')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', settings.LOGIN_REDIRECT_URL)
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'authenticate.html', {'username': username})
    else:
        return render(request, 'authenticate.html')
    


def student_register(request):
    return render(request, 'student_register.html')


def _hall(request):
    #students = Student.objects.all()
    halls = Hall.objects.all()
    images = HallImage.objects.all()
    return render(request, 'hallSelection.html', {'halls': halls, 'images':images})
    

@login_required
def _rooms(request,pk):
    hall = get_object_or_404(Hall,id=pk)
    images = HallImage.objects.filter(hall=hall)
    rooms = Room.objects.filter(hall=hall)
    return render(request, 'rooms.html', {'rooms': rooms, 'hall': hall, 'images': images})


@login_required
def _booking(request,room_id):
    if request.method == 'POST':
        student = get_object_or_404(Student,name=request.user.name)
        existing_booking = Room.objects.filter(student=student).exists()
        if existing_booking:
            messages.error(request, "You have already booked a room.")
            return redirect('booking_details')
        else:
            room = get_object_or_404(Room, id=room_id)
            booking = Booking.objects.create(room=room, student=student, hall=room.hall)
            booking.save()
            student.room = room
            student.save()

        messages.success(request, "Room booked successfully.")
        return redirect('booking_details')
    
        
    return render(request, 'rooms.html')
      
        
    



def hall_manager_home(request):
    return render(request, 'hall_manager_home.html')

@login_required
def _logout_user(request):
    logout(request)
    return redirect('index')

def _confirmation(request):
    booking = Booking.objects.all()
    return render(request, 'confirmation.html')


#stripe
@login_required
def _charge(request):
    
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
    
    
    # Verify if the user has a booking and if the booking is related to the requested room
    try:
        room = get_object_or_404(Room, id=request.user.room.id)
        booking = Booking.objects.get(student=request.user, room=room)
    except Booking.DoesNotExist:
        # Redirect to hall section page if the user does not have a booking for the requested room
        return redirect('halls')
    
    students = Student.objects.filter(room=room)
    bookings = Booking.objects.all()
    return render(request, 'booking.html', {'booking': booking, 'bookings': bookings, 'key': key, 'students': students, 'room': room})


    
@login_required
def _cancel_booking(request):
    booking = get_object_or_404(Booking,student=request.user.id)
    print(booking)
    booking.delete()
    return redirect('index')



def _help(request):
    return render(request, 'help.html')




#test view
def test(request):
    return render(request, 'hallSelection.html')





@login_required
def _chat(request):
    student = get_object_or_404(Student,name=request.user.name)
    room = get_object_or_404(Room, id=request.user.room.id)
    students = Student.objects.filter(room=room)
    return render(request, 'chatroom.html',{
        'student': student,'room':room, 'students': students
    })


@login_required
def _send(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        if not message:
            return HttpResponseBadRequest("Message cannot be empty")

        student = request.user
        room = get_object_or_404(Room, id=request.user.room.id)

        new_message = Message.objects.create(value=message, student=student, room=room)
        # Make sure this is for debugging purposes only, not necessary in the final code.

        return JsonResponse({"status": "success"})
    else:
        return HttpResponseBadRequest("Invalid request method")

@login_required
def _getMessages(request):
    username = request.user.username
    room = get_object_or_404(Room, id=request.user.room.id)
    messages = Message.objects.filter(room=room)
    return JsonResponse({"messages": list(messages.values()), "username": username})





def handler500(request):
    return render(request, '500.html', status=500)


def handler404(request):
    return render(request, '404.html', status=404)