
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import BookingForm


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def event(request):
    return render(request, 'event.html')

def events_details(request):
    return render(request, 'events_details.html')

def thanks(request):
    return render(request, 'thanks.html')

def success_view(request):
    return render(request, 'thanks.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # Process form (e.g., send email)
        send_mail(
            f"Message from {name}",
            message,
            email,
            ['prudhviteja2002@gmail.com'],  
        )
        return render(request, 'thanks.html')
    return render(request, 'contact.html')

from .models import Booking

def contact_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Save the data to the database
            Booking.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                mobile=form.cleaned_data['mobile'],
                from_location=form.cleaned_data['from_location'],
                to_location=form.cleaned_data['to_location'],
                date=form.cleaned_data['date'],
                members=form.cleaned_data['members'],
            )
            return redirect('thanks')  # Redirect to a success page
    else:
        form = BookingForm()

    return render(request, 'contact.html', {'form': form})
