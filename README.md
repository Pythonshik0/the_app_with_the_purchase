# Django + Stripe API Backend

## Описание

[Stripe](https://stripe.com/docs) - платежная система с подробным API и бесплатным тестовым режимом для имитации и тестирования платежей. С помощью библиотеки Stripe на Python вы можете удобно создавать платежные формы разных видов, сохранять данные клиента и реализовывать прочие платежные функции.

Мы предлагаем вам реализовать Django + Stripe API бэкенд с функционалом, описанным ниже.

## Задание

- **Модель Django Item**: поле (name, description, price).
  - GET /buy/{id}: Получение Stripe Session Id для оплаты выбранного Item.
  - GET /item/{id}: Получение HTML страницы с информацией о товаре и кнопкой "Buy".

> Пример использования методов API и дополнительные указания доступны [здесь](ссылка).

## Установка и Запуск

1. Склонируйте репозиторий:

bash
git clone https://github.com/Pythonshik0/the_app_with_the_purchase

2. Перейдите в папку проекта:

bash
cd project-directory

3. Запустите Docker контейнеры:

bash
docker-compose up -d --build

4. Примените миграции:

bash
docker-compose exec web python manage.py migrate --noinput

## Links

- [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) - Админ панель
- [http://127.0.0.1:8000/buy/<item_id>](http://127.0.0.1:8000/buy/<item_id>) - Получение Stripe Session Id
- [http://127.0.0.1:8000/item/<item_id>](http://127.0.0.1:8000/item/<item_id>) - Страница товара
