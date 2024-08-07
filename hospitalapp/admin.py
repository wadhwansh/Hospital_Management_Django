from django.contrib import admin
from hospitalapp.models import login,Contact,Booking
# Register your models here.
class Contact_admin(admin.ModelAdmin):
    list_display=('Name','Email','Subject','Phone','Message')
    
admin.site.register(Contact,Contact_admin)


class Booking_admin(admin.ModelAdmin):
    list_display=('Name','Email','Purpose','Surgury','Phone','Date','Time')

admin.site.register(Booking,Booking_admin)