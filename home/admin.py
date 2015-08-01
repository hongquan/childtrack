from django.contrib import admin

from .models import Child, Location, Activity

# Register your models here.
admin.site.register(Child)
admin.site.register(Location)
admin.site.register(Activity)
