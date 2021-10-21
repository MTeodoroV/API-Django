from rest_framework import serializers
from escola.models import Aluno, Curso

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento'] #Filtro de dados que queremos disponibilizar para a api

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso #Qual o modelo que estou utilizando
        fields = '__all__' #Todos os campos de curso
