# Система управления данными о сборке заказов

Этот проект представляет собой набор Python-скриптов для взаимодействия с PostgreSQL базой данных, используемой для отслеживания и управления данными о сборке заказов в интернет-магазине. Проект включает в себя запись данных, поиск, анализ, а также обновление информации. Для работы с базой данных используется библиотека `psycopg2`.

## Структура проекта

Проект состоит из следующих файлов и каталогов:

*   `db_config.py`:  Содержит настройки подключения к базе данных PostgreSQL.
*   `db_info.ini`:  Файл конфигурации с учетными данными для подключения к PostgreSQL.
*   `duplicates.py`: Скрипт для проверки наличия дубликатов заказов.
*   `start.py`:  Скрипт для записи времени начала сборки заказа.
*   `end.py`: Скрипт для записи времени окончания сборки заказа.
*   `info_order.py`: Скрипт для получения описательной статистики по заказам за определенный период.
*   `intokf.py`: Скрипт для записи информации о заказе.
*   `money.py`: Скрипт для записи суммы заказа.
*  `number_search.py`: Скрипт для поиска заказа по номеру.
*   `orders_today.py`: Скрипт для вывода списка заказов за текущий день.
*   `update.py`: Скрипт для обновления количества мест в заказе.
*   `jambs.py`: Скрипт для записи информации об ошибках при сборке заказа.
*   `repeated.py`: Скрипт для записи информации о повторных заказах или ошибках клиента.
* `_pycache_`: Каталог для кэшированных файлов Python.

## Настройка проекта

1.  **Установка зависимостей:**
    ```bash
    pip install psycopg2
    pip install python-dotenv
    ```
2.  **Конфигурация базы данных:**
    *   Создайте файл `db_info.ini` в корневой директории проекта и заполните его учетными данными вашей PostgreSQL базы данных.
    *   Пример содержимого `db_info.ini` см. ниже.
3.  **Настройка переменных окружения:**
   *  Можно использовать `.env` файл, если вы не хотите хранить данные в `db_info.ini`.

## Использование

Каждый скрипт выполняет определенную функцию:

*   **`duplicates.py`**:
    *   Проверяет и выводит информацию о дубликатах заказов на основе номера заказа и даты.
*  **`start.py`**:
    *  Записывает время начала сборки заказа в таблицу `time_start`.
*  **`end.py`**:
    * Записывает время окончания сборки заказа в таблицу `time_end`.
*   **`info_order.py`**:
    *   Получает и выводит описательную статистику по заказам (общее количество заказов, среднее количество мест, и т.д.) за определенный период.
*   **`intokf.py`**:
    *   Записывает данные о новых заказах в таблицу `kupiflakon`.
*   **`money.py`**:
    *   Записывает сумму заказа в таблицу `money`.
*   **`number_search.py`**:
    *   Ищет заказ по номеру и выводит его данные.
*   **`orders_today.py`**:
    *   Выводит список заказов, созданных за текущий день.
*   **`update.py`**:
    *   Обновляет количество мест в заказе по его ID.
*  **`jambs.py`**:
    *  Записывает информацию об ошибках при сборке заказа в таблицу `jambs`.
* **`repeated.py`**:
    *  Записывает информацию о повторных заказах или ошибках клиента в таблицу `repeated`.

Для запуска скриптов, используйте команду `python название_скрипта.py`

Пример: `python start.py`, `python info_order.py`

## Пример `db_info.ini`

```ini
[postgresql]
host = ваш_хост
database = ваша_база_данных
user = ваш_пользователь
password = ваш_пароль
port = ваш_порт

Лицензия
Этот проект не имеет лицензии.