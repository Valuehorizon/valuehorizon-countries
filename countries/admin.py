from django.contrib import admin
from countries.models import Country, City, Government, Region

class CountryAdmin(admin.ModelAdmin):
    search_fields = ["name",]
    list_display = ['common_name', 'name', 'symbol_alpha2_code', 'symbol_alpha3_code', 'iso_status']
    list_filter = ['iso_status']
admin.site.register(Country, CountryAdmin)

class CityAdmin(admin.ModelAdmin):
    search_fields = ["name",]
    list_display= ['name', 'country']
admin.site.register(City, CityAdmin)

class GovernmentAdmin(admin.ModelAdmin):
    search_fields = ["name",]
admin.site.register(Government, GovernmentAdmin)

class RegionAdmin(admin.ModelAdmin): 
    search_fields = ["name",]
    filter_horizontal = ('country',)
admin.site.register(Region, RegionAdmin)


