from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category)
admin.site.register(QuantityVariant)
admin.site.register(Product)
admin.site.register(Feedback)
admin.site.register(Order)
admin.site.register(OrderItem)