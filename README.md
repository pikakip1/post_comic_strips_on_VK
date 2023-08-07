# Публикация комиксов

Скрипт скачивает с сайта https://xkcd.com/ случайный комикс с подписью и выкладывает в группу ВК.  

## Установка

Создайте приложение для вашей группы, перейдите в управление и выберете состояние включенного приложения.

Скачайте архив, или сделайте клон репозитория в нужную директорию.

Установите библиотеки.

```
pip instal -r requirements.txt
```

Запустите скрипт авторизации для получения токена

```
python authorize.py
```

Перейдите по ссылке и скопируйте часть адресной строки от access_token= до &expires_in

## Настройка окружения

Создайте файл sensitive_information.env, и впишите переменные
```
ID_CLIENT=<id вашего приложения>
access_token=<токен вк>
id_group=<id группы>
```

Запустите скрипт для постинга комиксов

```
python main.py
```

Готово, пост с подписью автора выложен.