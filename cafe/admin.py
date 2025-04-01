from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Reservation, Contact, MenuCategory, MenuItem, Testimonial, Subscriber, GalleryImage, SpecialOffer

admin.site.register(Reservation)
admin.site.register(Contact)
admin.site.register(MenuCategory)
admin.site.register(MenuItem)
admin.site.register(Testimonial)
admin.site.register(Subscriber)
admin.site.register(GalleryImage)
admin.site.register(SpecialOffer)