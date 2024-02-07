# Описание
Сервис обрабатывает загруженные файлы в соответствии с их типом.

Технологии 
- Django
- Poetry
- Nginx
- Gunicorn
- Docker
- Celery
- RabbitMQ

# Установка

1. Клонируйте репозиторий с помощью SSH:
```bash
git clone git@github.com:pandenic/picasso_test_task.git
```

2. Перейдите в каталог проекта:
```bash
cd picasso_test_task
```

3. Создайте файл .env в корне проекта, используя шаблон /infra/.env.example


4. Запустите docker compose:
```bash
docker compose up -d
```

5. Сервер запускается по адресу http://localhost/

### Endpoints:

http://localhost/api/upload/ | Вы можете загрузить туда файл с помощью POST-запроса.
http://localhost/api/file/ | вы можете получить данные всех файлов из базы данных с помощью GET запроса.

# Deploy

Deploy с помощью доступных GitHub Actions.
(pipline в .github/workflows/main.yml)

---

# Description
Service process uploaded files according to their file type.

Technologies 
- Django
- Poetry
- Nginx
- Gunicorn
- Docker
- Celery
- RabbitMQ

# Installation

1. Clone repository with SSH:
```bash
git clone git@github.com:pandenic/picasso_test_task.git
```

2. Go to the project directory:
```bash
cd picasso_test_task
```

3. Create .env file in root using template /infra/.env.example


4. Run docker compose:
```bash
docker compose up -d
```

5. Server starts at http://localhost/

### Endpoints:

http://localhost/api/upload/ | you could upload file there with POST request
http://localhost/api/files/ | you could get all files data from database with GET request

# Deploy

Deploy with GitHub Actions available.
(pipline in .github/workflows/main.yml)
