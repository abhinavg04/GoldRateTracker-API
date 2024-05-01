from django.contrib import admin
from .models import GoldRate
# Register your models here.
class GoldAdmin(admin.ModelAdmin):
    list_display=['added_date','category']
admin.site.register(GoldRate,GoldAdmin)