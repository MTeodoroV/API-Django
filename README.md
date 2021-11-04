# API-Django

<h3>Configurando um projeto django</h3>

1- Criando um ambiente virtual:
```
  python3 -m venv ./venv
```

2- Ativando o ambiente virtual (Windows): 
```
  venv\Scripts\activate.bat
```

 Ativando o ambiente virtual (Mac ou Linux): 
```
  source venv/bin/activate
```

3- Instalar o django no ambiente virtualizado:
```
  pip install django
````

4- Criando um projeto chamado setup com o django admin para manter toda a configuração da aplicação:
```
  django-admin startproject setup .
```

5- Pasta setup alterar o arquivo settings.py com os dados abaixo:
```
  LANGUAGE_CODE = 'pt-br'
  TIME_ZONE = 'America/Sao_Paulo'
```

<h3>Criando o projeto</h3>

1- Segue o comando para criar um projeto:
```
  python manage.py startapp nomedoprojeto
```

2- Instalando o django rest framework:
```
  pip install djangorestframework
```

3- Instalando o markdown:
```
  pip install markdown 
```

4- Adicionando o rest_framework nos INSTALLED_APPS: 
```
   'rest_framework', 
```
