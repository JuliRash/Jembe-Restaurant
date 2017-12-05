from django.contrib import admin
from project.models import Reservation, User
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'email', 'people', 'time', 'phone',
                    'date_reserved', 'status']


class MyUserAdmin(UserAdmin):
    model = User

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('picture',)}),
    )


admin.site.register(User, MyUserAdmin)
admin.site.register(Reservation, ReservationAdmin)
