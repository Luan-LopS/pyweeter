# PROJETO PYWEET

Projeto de conclusão de curso de full stack Python, realizado pela EBAC, o desafio contituia em desenvolver prototipo do tweeter, o backend foi desenvolvido com Python com django-rest-framework.

### Resquisitos
* Python 3.8+
* Django 5.2*


### Instalação
-    Etapa 1

Para realizar o clone do projeto, após isso entre no diretorio: 

            git clone https://github.com/Luan-LopS/pyweeter.git
            cd pyweeter

-   Etapa 2

Criar e ative o ambiente virtual: 

            python -m venv venv
            
            # windows
            . venv/bin/activate

            # 
            . venv\Scripts\activate

-   Etapa 3:

Istalar dependencias:

            pip install -r requirements.txt

-   Etapa 4:

Criar arquivos de variaveis de ambiente, no diretorio raiz crie o arquivo .env, dentro do mesmo configuraremos as as variaveis SECRET_KEY e ALLOW_HOSTS:

            #.env

            SECRET_KEY=suaSecretKey
            ALLOW_HOSTS=localhost,127.0.0.1

-   Etapa  5:

Consfiguração de banco de dados, não  é necessario no nosso caso, pois utilizamos o SQLite.

-   Etapa 6:

Migrações

            python manage.py migrate

-   Etapa 7:

Iniciar o servidor:

            python manage.py runserver




