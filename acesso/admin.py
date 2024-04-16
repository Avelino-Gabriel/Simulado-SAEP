from django.contrib import admin
from .models import Professor, Atividade, Turma

# Register your models here.
admin.site.register(Professor)
admin.site.register(Atividade)
admin.site.register(Turma)
