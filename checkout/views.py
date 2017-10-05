from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, AddressForm
from django.conf import settings
from products.models import Product
import stripe

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    if request.method=="POST":
        address_form = AddressForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if address_form.is_valid() and payment_form.is_valid():
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price

            try:
                customer = stripe.Charge.create(
                    amount= int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        address_form = AddressForm()

    return render(request, "checkout.html", {'address_form': address_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE })
