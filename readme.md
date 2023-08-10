## Развёртывание

1. В терминале из корня проекта
    ```
    $ pip install poetry
    $ poetry install
    ```
2. (Только при развертывании на локальной машине)
    ```
   Установить и настроить бд MySQL
   Поменять поля NAME, USER и PASSWORD в DATABASES в файле settings.py
   ```
3. Миграции
   ```
   $ cd shop/
   $ python manage.py migrate   
   ```
4. Дамп
   ```
   1. загрузить из файла
       $ python manage.py loaddata db.json
   2. создать свой
       $ python manage.py dumpdata > db.json
   ```