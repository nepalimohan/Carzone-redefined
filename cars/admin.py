from django.contrib import admin
from cars.models import Car
from django.utils.html import format_html


# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object): #object contains teams data
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.car_photo.url))

    thumbnail.short_description = "CarImage"
    
    list_display = ['id','thumbnail', 'car_title', 'color', 'model', 'year','body_style', 'fuel_type', 'city', 'is_featured']
    list_display_links = ['id','thumbnail','car_title',]
    list_editable = ('is_featured',)
    search_fields = ('id','car_title','city', 'model','year','body_style', 'fuel_type')
    list_filter = ('city','model','body_style', 'fuel_type')
