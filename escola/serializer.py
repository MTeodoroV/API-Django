from django.db.models import fields
from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento'] #Filtro de dados que queremos disponibilizar para a api

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso #Qual o modelo que estou utilizando
        fields = '__all__' #Todos os campos de curso

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = [] #Trazer tudo exceto o que eu passar em exclude

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome']