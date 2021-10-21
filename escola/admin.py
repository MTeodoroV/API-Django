from django.contrib import admin
from escola.models import Aluno, Curso

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome') #Quando fazer alguma alteração posso clicar e ser direcionado;
    search_fields = ('nome',) #Campo de busca por nome;
    list_per_page = 20

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)

admin.site.register(Curso, Cursos)
