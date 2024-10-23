from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada")
    list_display_links = ("id", "nome")
    search_fields = ("nome",) #campo de busca para buscar pelo nome
    #a vírgula no final é porque precisa ser uma tupla
    list_filter = ("categoria",)
    list_editable = ("publicada",)
    list_per_page = 10
    
admin.site.register(Fotografia, ListandoFotografias)
