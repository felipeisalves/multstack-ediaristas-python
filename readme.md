# Projeto e-diaristas

### Instalando o projeto

### Clonar o projeto
`git clone https://github.com/felipeisalves/multstack-ediaristas-python.git`

### Instalar dependências
`pip install -r requirements.txt`

### Alterar configurações do BD no arquivo settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_db',
        'HOST': '_do_db_db',
        'PORT': porta_do_db,
        'USER': 'usuario_do_db',
        'PASSWORD': 'senha_db'
    }
}
```

### Migrar banco de dados
`python manage.py migrate`

### Iniciar o servidor
`python manage.py runserver`