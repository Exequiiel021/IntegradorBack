from django.contrib import admin
from .models import Receta

class ContenidoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') 

# Register your models here.
admin.site.register(Receta, ContenidoAdmin)
