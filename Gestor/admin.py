from django.contrib import admin
from .models import Estante,Cargo, Oficina, Empresa, Empleado
from django.utils.html import format_html


@admin.register(Empresa)
class GestionEmpresa(admin.ModelAdmin):
   list_display = ( 'id','nempresa', 'imgref', 'Logo',)
   list_display_links = ('nempresa',)

   def Logo(self, obj):
    return  format_html('<img src ={} width=80 />',obj.imgref.url)


@admin.register(Empleado)
class GestionEmpleado(admin.ModelAdmin):
    list_display = ('status','cedula', 'primerApellido', 'primerNombre',)
    list_filter = ('status', 'genero',)
    search_fields = ('cedula', 'primerApellido', 'primerNombre',)
    list_display_links = ('cedula',)
    list_per_page = 5


@admin.register(Estante)
class GestionEstante(admin.ModelAdmin):
    list_display = ('ubicacion',)
    list_display_links = ('ubicacion',)


@admin.register(Oficina)
class GestionOficina(admin.ModelAdmin):
    list_display = ('noficina',)
    list_display_links = ('noficina',)



@admin.register(Cargo)
class GestionCargo(admin.ModelAdmin):
    list_display = ('cargo',)
    list_display_links = ('cargo',)
