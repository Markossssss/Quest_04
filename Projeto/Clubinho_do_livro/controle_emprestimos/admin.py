from django.contrib import admin
from .models import *

#class CaixaInline(admin.TabularInline):
#    model = Caixa

#class AmigoInline(admin.TabularInline):
#    model = Amigo

#class RevistaAdmin(admin.ModelAdmin):
#    inlines = [
#        CaixaInline,
#        AmigoInline,
#    ]

admin.site.register(Caixa)
admin.site.register(Amigo)
admin.site.register(Colecao)
admin.site.register(Revista)
admin.site.register(Emprestimo)

# Register your models here.
