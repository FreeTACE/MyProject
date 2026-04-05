import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyProject.settings')
django.setup()

from trening.models import Category, Lesson, Card

# Создаем категории
categories_data = [
    {
        'name': 'Основы Python',
        'slug': 'osnovy-python',
        'description': 'Изучите основы программирования на языке Python: переменные, типы данных, условные операторы, циклы и функции.',
        'order': 1,
    },
    {
        'name': 'Веб-разработка на Django',
        'slug': 'django-development',
        'description': 'Создание веб-приложений с помощью фреймворка Django: модели,视图, шаблоны, админ-панель.',
        'order': 2,
    },
]

for cat_data in categories_data:
    category, created = Category.objects.get_or_create(
        slug=cat_data['slug'],
        defaults=cat_data
    )
    print(f"{'Создана' if created else 'Обновлена'} категория: {category.name}")

# Создаем уроки
lessons_data = [
    {
        'category_slug': 'osnovy-python',
        'name': 'Введение в Python',
        'slug': 'python-intro',
        'description': 'История Python, установка, первая программа',
        'content': '<h2>Python - это просто!</h2><p>Python - это высокоуровневый язык программирования.</p>',
        'order': 1,
    },
    {
        'category_slug': 'osnovy-python',
        'name': 'Переменные и типы данных',
        'slug': 'variables-and-types',
        'description': 'Изучение переменных и типов данных',
        'content': '<h2>Типы данных</h2><p>В Python есть int, float, str, bool и другие.</p>',
        'order': 2,
    },
]

for lesson_data in lessons_data:
    category = Category.objects.get(slug=lesson_data['category_slug'])
    lesson, created = Lesson.objects.get_or_create(
        slug=lesson_data['slug'],
        defaults={
            'category': category,
            'name': lesson_data['name'],
            'description': lesson_data['description'],
            'content': lesson_data['content'],
            'order': lesson_data['order'],
        }
    )
    print(f"{'Создан' if created else 'Обновлен'} урок: {lesson.name}")

# Создаем карточки
cards_data = [
    {
        'lesson_slug': 'python-intro',
        'question': 'Кто создал язык Python?',
        'answer': 'Гвидо ван Россум',
        'hint': 'Голландский программист',
        'order': 1,
    },
    {
        'lesson_slug': 'python-intro',
        'question': 'В каком году был создан Python?',
        'answer': '1991',
        'hint': 'Начало 90-х годов',
        'order': 2,
    },
    {
        'lesson_slug': 'variables-and-types',
        'question': 'Какой тип данных используется для целых чисел в Python?',
        'answer': 'int',
        'hint': 'Сокращение от integer',
        'order': 1,
    },
    {
        'lesson_slug': 'variables-and-types',
        'question': 'Как объявить переменную name со значением "Alice" в Python?',
        'answer': 'name = "Alice"',
        'hint': 'Используйте оператор присваивания',
        'order': 2,
    },
]

for card_data in cards_data:
    lesson = Lesson.objects.get(slug=card_data['lesson_slug'])
    card, created = Card.objects.get_or_create(
        lesson=lesson,
        question=card_data['question'],
        defaults={
            'answer': card_data['answer'],
            'hint': card_data['hint'],
            'order': card_data['order'],
        }
    )
    print(f"{'Создана' if created else 'Обновлена'} карточка: {card.question[:30]}")

print("Тестовые данные успешно добавлены!")