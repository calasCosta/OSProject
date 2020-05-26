from django.contrib import admin
from .models import Pet #colocamos só .models porque o arquivo admin está na mesma pasta que models
# Register your models here.

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['id', 'city', 'description', 'user']

