from django.contrib import admin
from .models import Tipo_articulo, Acta_congreso, Articulo, Autor, Informe_tecnico, Group_Invest, Revista_cientifica
# Register your models here.

admin.site.register(Tipo_articulo)
admin.site.register(Acta_congreso)
admin.site.register(Articulo)
admin.site.register(Autor)
admin.site.register(Informe_tecnico)
admin.site.register(Group_Invest)
admin.site.register(Revista_cientifica)