from django.contrib import admin
from jembe.models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone',
                    'subject', 'message', 'date_sent'
                    ]
    search_fields = ['name', 'email']


admin.site.register(Contact, ContactAdmin)
