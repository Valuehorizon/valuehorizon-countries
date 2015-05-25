from django.contrib import admin
from countries.models import Country, City, Government, Region


admin.site.register(Country)
admin.site.register(City)
admin.site.register(Government)

class RegionAdmin(admin.ModelAdmin): 
    filter_horizontal = ('country',)
admin.site.register(Region, RegionAdmin)


