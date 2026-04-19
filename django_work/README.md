# Django Project

## Описание

Это проект блога на Django.

## Функции
- Регистрация и авторизация
- Создание, редактирование и удаление постов
- Просмотр списка постов
- Редактирование профиля
- Возможность оставлять комментарии

## Установка и настройка

### Клонирование репозитория
```bash
git clone https://github.com/project-name-link.git
cd django_work
```
### Создание виртуального окружения
```bash
python -m venv venv
source venv/bin/activate
venv/Scripts/activate # Для windows
```
### Установка зависимостей
```bash
pip install -r requirement.txt
```

### Приминение миграций
```bash
python manage.py migrate
```
### Создание суперпользователя
```bash
python manage.py createsuperuser
```
### Запуск сервера
```bash
python manage.py runserver
```

## Основные страницы

- Главная страница: http://127.0.0.1:8080/
- Детали поста: http://127.0.0.1:8080/detail/<id>/
- Создание поста: http://127.0.0.1:8080/create/
- Редактирование поста: http://127.0.0.1:8080/update/<id>
- Профиль пользователя: http://127.0.0.1:8080/profile

## Тестирование

```bash
python manage.py test blog
```
