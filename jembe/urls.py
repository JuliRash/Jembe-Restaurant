from django.conf.urls import url
from jembe import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^reservation/$', views.NewReservation.as_view(), name="reservation"),
    url(r'^contact/$', views.Contact.as_view(), name="contact"),
    url(r'^payments/$', views.payment, name="payment"),
]