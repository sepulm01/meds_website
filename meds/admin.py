from django.contrib import admin
from meds.models import *
# Register your models here.

admin.site.site_header = "Meds"
admin.site.index_title = "Menú"
admin.site.site_title = 'Meds'

class PrevInline(admin.TabularInline):
    model = Prevision
    extra = 0
    list_display = ['nom_prev']

class Contacline(admin.TabularInline):
    model = Contacto
    extra = 0
    list_display = ['nombre','fono', 'parentesco']

class Medicline(admin.TabularInline):
    model = Medicamentos
    extra = 0
    list_display = ['med_nom','dosis', ]

class Alerline(admin.TabularInline):
    model = Alergias
    extra = 0
    list_display = ['nom_aler', ]



@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellido','rut','edad','sexo']
    inlines = [Contacline, PrevInline, Medicline, Alerline ]
    fieldsets = (
        ('REQUERIMIENTO', {
                            #'fields': ('autor','estado','operador',( 'tipo','clasifi', 'urgencia'),
                            'fields': ('nombre', 'apellido','rut', 'edad','sexo','fono','sangre','direccion','pais','region','provincia','comuna'),},),
        )

#admin.site.register(Pais)

#admin.site.register(Region)

#admin.site.register(Prov)

#admin.site.register(Comuna)

admin.site.register(Contacto)

admin.site.register(Prevision)