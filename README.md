_Репозиторий на Github [ссылка](https://github.com/JuliaBars/fullstack_app_todo_FastApi)._

## Fullstack приложение на FastAPI для создания списков дел

---
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![Postgres](https://img.shields.io/badge/Alembic-008756?style=for-the-badge&logo=alembic)

---


Склонируйте проект и установите зависимости.
```
pip install -r requirements.txt
```
Для исспользования Postgres в файле database.py укажите путь до БД в переменной SQLALCHEMY_DATABASE_URL.
В engine необходимо убрать connect_args, тк это используется только для SQLite3.

Заполните файл .env по образцу или используйте значения по умолчанию.
```
SECRET_KEY=
ALGORITHM=
```

Запустите сервер
```
uvicorn main:app --reload
```

_автор Юлия Орлова_
