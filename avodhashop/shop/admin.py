from django.contrib import admin
from.models import *

# Register your models here.
class catagdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug']
admin.site.register(categ,catagdmin)


class proAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug','price','stock','img','available']
    list_editable=['price','stock','img','available']
admin.site.register(products,proAdmin)
