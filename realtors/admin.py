from django.contrib import admin
from django.db import models
from . models import Realtor

# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','phone','hire_date','is_mvp')
    list_display_links = ('id','name')
    list_editable = ('email','phone','is_mvp')
    search_fields = ('name',)


admin.site.register(Realtor, RealtorAdmin)