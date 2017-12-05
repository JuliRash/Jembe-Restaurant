from django import forms
from project.models import Reservation
from jembe.models import Contact


class ReservationForm(forms.ModelForm):
    date_reserved = forms.DateField(widget=forms.TextInput(
        attrs={}), required=True,)
    email = forms.EmailField(widget=forms.TextInput
                             (attrs={'id': 'reservation_email',
                                     'placeholder': "Your Email"}))
    time = forms.TimeField(
        widget=forms.TextInput(attrs={'id': 'reservation_time',
                                      'placeholder': "Expected time"}))

    comment = forms.CharField(widget=forms.Textarea(
        attrs={'col': '30', 'rows': '10', 'placeholder': 'comment'}))
    phone = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Phone No start with +234',
               'id': 'reservation_phone',
               }), required=True,)

    class Meta:
        model = Reservation
        fields = ['first_name', 'last_name',
                  'email', 'people', 'time',
                  'phone', 'date_reserved', 'status', 'comment']
        exclude = ['last_name', 'status']


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'subject', 'message']
