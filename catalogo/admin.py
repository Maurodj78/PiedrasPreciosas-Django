from django.contrib import admin
from .models import Producto

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('create','update')

admin.site.register(Producto, ProductoAdmin)
