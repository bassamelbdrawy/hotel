from django.contrib import admin
from .models import hotels,units,reviews,books,orders,user_information

admin.site.register(hotels)
admin.site.register(units)
admin.site.register(reviews)
admin.site.register(books)
admin.site.register(orders)
admin.site.register(user_information)
