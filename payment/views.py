from django.shortcuts import render
import stripe
from django.conf import settings
from django.http import JsonResponse
from .models import Payment
from django.views.generic import TemplateView, View

stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        #room_id = request.POST.get('room_id')
        #room = Room.objects.get(id=room_id)
        #payment = Payment.objects.create(room=room, price=room.price)
        #payment.save()
        price = Payment.objects.get(id=self.kwargs['pk']) 
        domain = settings.YOUR_DOMAIN
        if settings.DEBUG:
            domain = 'http://127.0.0.1:8000'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=domain + '/success/',
            cancel_url=domain + '/cancel/',
        )
        return redirect(checkout_session.url )
    



class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelView(TemplateView):
    template_name = 'cancel.html'