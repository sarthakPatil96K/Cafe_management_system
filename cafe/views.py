import datetime
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def menu(request):
    return render(request, 'menu.html')


def testimonial(request):
    return render(request, 'testimonial.html')

 


from django.shortcuts import render, redirect
from .forms import ReservationForm, ContactForm, SubscribeForm
from .models import Reservation, Contact, Subscriber

from datetime import datetime, timedelta


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ReservationForm

from django.contrib import messages

def reservation(request):
    max_date = (datetime.now() + timedelta(days=90)).strftime('%Y-%m-%d')

    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.status = 'pending'
            reservation.save()
            messages.success(request, "Your reservation has been booked successfully!")
            form = ReservationForm()  # Clear the form
    else:
        form = ReservationForm()
    
    return render(request, 'reservation.html', {
        'form': form,
        'max_date': max_date
    })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})  # For AJAX handling
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to home after subscription
    return redirect('index')  # Fallback redirect