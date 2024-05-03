from django.contrib import admin
from .models import Contact
models = [Contact]
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number')
    list_filter = ('last_name', 'phone_number', 'owner')
    search_fields = ('last_name', 'phone_number', 'owner')
    ordering = ('last_name', 'phone_number', 'owner')
admin.site.register(models, ContactAdmin)