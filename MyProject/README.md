# 📚 MyProject - Платформа для обучения (Trening App)

Добро пожаловать в **Сайт образовательной среды** — веб-приложение для эффективного обучения. 
Платформа объединяет учебные карточки (карты), категории, интерактивные викторины и структурированные 
уроки для лучшего усвоения материала.

## ✨ Возможности

- 📂 **Категории** — организация учебных материалов по темам.
- 🃏 **Карточки (Karti)** — простой способ запоминания информации (термин/определение).
- 🎯 **Викторины (Quiz)** — проверка знаний с подсчетом результатов.
- 📖 **Уроки (Lessons)** — детальное изучение тем с разбивкой по страницам.
- 📱 **Адаптивный дизайн** — базовые шаблоны на основе Bootstrap/HTML.
- 📊 **Результаты викторин** — сохранение и отображение статистики.

## 🛠 Технологии

- **Backend:** Django (Python)
- **Database:** SQLite (по умолчанию, можно заменить на PostgreSQL)
- **Frontend:** HTML, Bootstrap (подразумевается структурой шаблонов)
- **ORM:** Django Models

## 📁 Структура проекта

MyProject/
├── MyProject/ # Основная конфигурация Django
│ ├── init.py
│ ├── settings.py # Настройки проекта
│ ├── urls.py # Главные маршруты
│ ├── asgi.py / wsgi.py
├── trening/ # Основное приложение
│ ├── migrations/ # Миграции БД
│ ├── templates/trening/ # HTML-шаблоны
│ │ ├── base.html
│ │ ├── home.html
│ │ ├── cards_list.html
│ │ ├── categories.html
│ │ ├── category_detail.html
│ │ ├── karti.html
│ │ ├── lesson_detail.html
│ │ ├── quiz.html
│ │ ├── quiz_results.html
│ │ └── help.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py # Модели (Категории, Карточки, Уроки, Квизы)
│ ├── views.py # Логика обработки запросов
│ ├── urls.py # Маршруты приложения
│ ├── create_test_data.py # Скрипт для генерации тестовых данных
├── db.sqlite3 # База данных
├── manage.py # Утилита управления Django


## 🚀 Быстрый старт

### 1. Клонирование репозитория

git clone https://github.com/yourusername/MyProject.git
cd MyProject

2. Создание виртуального окружения
python -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate     # Для Windows

3. Установка зависимостей
pip install django
# Если используете другие пакеты (Pillow, psycopg2 и т.д.) — добавьте их сюда

4. Применение миграций
python manage.py migrate

5. Заполнение тестовыми данными (опционально)
python manage.py shell < trening/create_test_data.py
# Или запустить скрипт вручную через Django shell

6. Запуск сервера
python manage.py runserver

Откройте браузер и перейдите по адресу: http://127.0.0.1:8000

🧩 Использование
Главная страница (home.html) — приветствие и навигация.

Категории — просмотр всех тем.

Карточки — просмотр и изучение карточек (karti.html и cards_list.html).

Уроки — детальный материал с возможностью перехода к следующему уроку.

Викторины — вопросы по выбранной категории, результат отображается на отдельной странице.

📝 API эндпоинты (если реализованы)
Если в urls.py и views.py есть API, опишите их здесь. По умолчанию — только стандартные Django views.

URL	Описание
/	Главная
/categories/	Список категорий
/category/<slug:category_slug>/	Детали категории
/cards/	Список всех карточек
/cards/quiz/<int:lesson_id>/	Запуск викторины
/category/<slug:category_slug>/lesson/<slug:lesson_slug>/	Страница урока
/help/	Справка

🔧 Настройка
Основные параметры находятся в MyProject/settings.py:

DATABASES — по умолчанию SQLite.

STATIC_URL и MEDIA_URL — при необходимости.

TEMPLATES — уже настроены для использования папки templates/.

🤝 Как внести вклад
1) Форкните проект.

2) Создайте ветку для новой функции (git checkout -b feature/AmazingFeature).

3) Зафиксируйте изменения (git commit -m 'Add some AmazingFeature').

4) Отправьте ветку (git push origin feature/AmazingFeature).

5) Откройте Pull Request.

📞 Контакты
Ваше Имя — @leodance28 — телеграм

Ссылка на проект: https://github.com/leodance24-sudo/MyProject/tree/master/MyProject

