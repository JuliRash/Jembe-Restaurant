from django.conf.urls import url

from project import views

urlpatterns = [
    url(r'^profile/$', views.Profile.as_view(), name="profile"),
    url(r'^add-reservation/$', views.AddReservation.as_view(), name="add"),
    url(r'^login/$', views.Login.as_view(), name="login"),
    # url(r'^register/$', views.Register.as_view(), name="register"),
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'^logout/$', views.LogoutView.as_view(), name="logout"),
    url(r'^view-reservations/$',
        views.view_reservations, name="view_reservations"),
    url(r'^update-reservation/(?P<pk>\d+)/$',
        views.UpdateReservation.as_view(), name="update_reservation"),
]
