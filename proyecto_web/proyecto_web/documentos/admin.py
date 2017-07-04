# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
#importar modelo
from documentos.models import Documento
#crear subclase de admin
class documentoAdmin(admin.ModelAdmin):
	model = Documento

#registrar model admin
admin.site.register(Documento, documentoAdmin)
