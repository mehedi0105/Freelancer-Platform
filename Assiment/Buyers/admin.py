from django.contrib import admin
from . import models
# Register your models here.

class category_admin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


admin.site.register(models.Category, category_admin)
admin.site.register(models.AddJob)
admin.site.register(models.Reveiw)
