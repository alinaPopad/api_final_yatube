# API для блога.
## Как это работает
В данном репозитории описан промежуточный вариант API для моего проекта небольшой социальной сети.
API реализовано согласно документации, предоставленной к проекту в формате Redoc. Аутентификация реализована с импользованием 
JWT токена.
## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:git@github.com:alinaPopad/api_final_yatube.git

git clone 
cd api_final_yatube
Cоздать и активировать виртуальное окружение:

python3 -m venv env
source env/bin/activate
Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip
pip install -r requirements.txt
Выполнить миграции:

python3 manage.py migrate
Запустить проект:

python3 manage.py runserver

## Технологии

Django==3.2.16
pytest==6.2.4
pytest-pythonpath==0.7.3
pytest-django==4.4.0
djangorestframework==3.12.4
djangorestframework-simplejwt==4.7.2
Pillow==9.3.0
PyJWT==2.1.0
requests==2.26.0
djoser

## Автор
Алина Попадченко
