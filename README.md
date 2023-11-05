# Сервис отслеживания курсов валют на основе KZT

## Как развернуть проект
- скачать репозиторий

- заполнить переменные среды заполнив файл ```.env```

- собрать и запустить докер-сборку

```docker-compose up -d --build```

```docker-compose up```

- создайте суперпользователя в консоли docker и зайдите в админку django

- http://localhost:8000/admin/

- зарегистрируйте нового пользователя и авторизуйтесь через swagger:

- http://localhost:8000/swagger/

- выданный токен с авторизации следует сохранить, для дальнейших действий можно использовать PostMan 
