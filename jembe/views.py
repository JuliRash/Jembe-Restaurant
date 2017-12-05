from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib import messages

from jembe.forms import ReservationForm, ContactForm


def home(request):
    return render(request, "index.html")


class NewReservation(CreateView):
    template_name = "reservation.html"
    form_class = ReservationForm

    def form_valid(self, form):
        new = form.save(commit=False)
        new.save()
        # sends a flash message to the user
        messages.success(
            self.request,
            "you have successfully booked a new" +
            " table confirm your by paying for the table ")
        # redirect the user back to his/her dashboard
        return redirect("/payments")


class Contact(CreateView):
    template_name = "contact.html"
    form_class = ContactForm

    def form_valid(self, form):
        new = form.save(commit=False)
        new.save()
        # send a flash message to the user
        messages.success(
            self.request,
            "your message was sent successfully")
        # redirect the user back to contact page
        return redirect("/contact")


def payment(request):
    return render(request, "payment.html")
