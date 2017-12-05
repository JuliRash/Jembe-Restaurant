from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import View, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import UpdateView
from project.forms import UpdateUser, ReservationForm, LoginForm, RegisterForm
from django.contrib import messages

from project.models import User, Reservation


class Profile(LoginRequiredMixin, UpdateView):
    """admin user view and update profile"""
    form_class = UpdateUser
    model = User
    template_name = "super/profile.html"
    login_url = "/login/"

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request, ("your profile has been updated successfully"))
        return redirect('/profile')


"""
registeration view remove comment to use and add 
url(r'^register/$', views.Register.as_view() name='register')
in the urls.py file (project) to use
class Register(View):
    form_class = RegisterForm
    template_name = "auth/register.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            messages.success(request,
                             "your account has been created successfully")
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if user.user_type == 'guest':
                        return redirect('/resturant')
                    elif user.user_type == 'admin':
                        return redirect('/dashboard')
        return render(request, self.template_name, {'form': form})"""


class Login(View):
    """ Login View."""
    form_class = LoginForm
    template_name = "auth/login.html"

    def get(self, request):
        logout(request)
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            messages.success(request, "you have logged in successfully ")
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/dashboard')
            else:
                error = "username or password is incorrect"
        return render(
            request, self.template_name, {'form': form, 'error': error})


class LogoutView(View):
    """ Custom Logout View."""
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/login')


@login_required(login_url="/login/")
def dashboard(request):
    """Admin dashboard view."""
    reservations = Reservation.objects.all()
    users = User.objects.all()
    pending = Reservation.objects.filter(status="pending")
    confirmed = Reservation.objects.filter(status="confirmed")
    return render(request, "super/dashboard.html",
                  {'users': users,
                   'reservations': reservations,
                   'pending': pending, 'confirmed': confirmed})


class AddReservation(LoginRequiredMixin, CreateView):
    """Admin user add new reservation."""
    template_name = "super/new_reserve.html"
    form_class = ReservationForm
    login_url = '/login/'

    def form_valid(self, form):
        new = form.save(commit=False)
        new.save()
        # send a flash message to the user
        messages.success(
            self.request,
            "you have successfully added a new table reservation ")
        # redirect the user back to his/her dashboard
        return redirect("/dashboard")


class UpdateReservation(LoginRequiredMixin, UpdateView):
    """Admin user updates all the reservation."""
    form_class = ReservationForm
    template_name = "super/update_reserve.html"
    model = Reservation

    def get_object(self, *args, **kwargs):
        obj = get_object_or_404(Reservation, pk=self.kwargs['pk'])
        return obj

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request, "you have successfully updated the reservation")
        return redirect('/dashboard')


@login_required(login_url="/login/")
def view_reservations(request):
    """Admin user view all the reservations."""
    reservations = Reservation.objects.all()
    return render(request,
                  "super/view_reserve.html",
                  {'reservations': reservations})
