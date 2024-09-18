from django.shortcuts import render, get_object_or_404, redirect
from .models import Flight
from .forms import FlightForm, AdminLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.http import require_POST


# Admin login view
def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_superuser:  # Ensure the user is an admin
                login(request, user)
                return redirect('admin_dashboard')  # Redirect to admin_dashboard
            else:
                messages.error(request, 'Invalid credentials or not an admin.')
    else:
        form = AdminLoginForm()

    return render(request, 'admin_login.html', {'form': form})


# Search flights by ID or other criteria
def search_flight(request):
    flight_id = request.GET.get('flight_id')
    flights = Flight.objects.filter(flight_id=flight_id) if flight_id else []
    return render(request, 'search_flight.html', {'flights': flights})


# List all flights
def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'flight_list.html', {'flights': flights})


# Add a new flight
def flight_create(request):
    if request.method == "POST":
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flight_list')
    else:
        form = FlightForm()
    return render(request, 'flight_form.html', {'form': form})


def edit_flight(request, flight_id):
    flight = get_object_or_404(Flight, flight_id=flight_id)

    if request.method == 'POST':
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('flight_list')  # Redirect to the list of flights or another appropriate page
    else:
        form = FlightForm(instance=flight)

    return render(request, 'edit_flight.html', {'form': form, 'flight': flight})


def delete_flight(request, flight_id):
    flight = get_object_or_404(Flight, flight_id=flight_id)

    if request.method == 'POST':
        flight.delete()
        return redirect('flight_list')  # Redirect to the list of flights or another appropriate page

    return render(request, 'delete_flight.html', {'flight': flight})


def homepage(request):
    return render(request, 'homepage.html')


def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')