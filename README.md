# Django-приложение “Образовательные модули”

Данный проект представляет собой веб-приложение для публикации образовательных модулей
## О проекте

Проект состоит из бэкенд-части на основе Django Rest Framework. Бэкенд обеспечивает работу API. Проект имеет возможность развертывания с помощью Docker.

#### Возможности

	Создание, чтение, обновление и удаление  образовательных модулей
	Просмотр списка  образовательных модулей
 
#### Технологии

	python==3.12
 	pip==24.0 python-dotenv==1.0.1
 	Django==5.0.6
	djangorestframework==3.15.1
	drf-yasg==1.21.7
	django-cors-headers==4.3.1
	coverage==7.5.1
	eventlet==0.36.1
 	psycopg-binary==3.1.19
	setuptools==69.5.1
	requests==2.31.0
	flake8==7.0.0
	


#### Запуск проекта

Склонируйте этот репозиторий

В проекте используется виртуальное окружение venv. При развертвывнии в Docker зависимости установятся автоматически.

#### При локальном развертывании, необходимо зависимости нужно установить командой:
	pip install -r requirements.txt

### Переименуйте файл .env.sample в корневой директории в .env и заполните необходимые переменные окружения


Примените миграции:
    
	python3 manage.py migrate

Запустите сервер:
    
	python3 manage.py runserver


Используйте команду для создания тестового суперпользователя, для входа в административную панель 
    
	python manage.py createsuperuser


#### Для запуска проекта через Docker необходимо:

Выполнить команды:

	docker-compose up -d --build - сборка образа и запуск контейнера
 
#### Документация API

	Документация API доступна после запуска сервера по адресу: http://localhost:8000/redoc/ или http://localhost:8000/swager/ (локально)  | http://0.0.0.0:8000/redoc/ или http://0.0.0.0:8000/swager/ (Docker)
