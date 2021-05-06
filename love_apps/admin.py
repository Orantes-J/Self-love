from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Product)

admin.site.register(TopPicks)

admin.site.register(NewArrivals)

admin.site.register(ComingSoon)

admin.site.register(BestSeller) 