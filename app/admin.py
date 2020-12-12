
from .models import Event
from django.contrib import admin
# from userAccount.models import User
class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['title']}),
    ]


# Register your models here.
admin.site.register(Event)
#admin.site.register(User)