from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db import models  # Добавьте эту строку!
from django.db.models import Count
from .models import Category, Lesson, Card


def home(request):
    """Главная страница"""
    categories = Category.objects.filter(is_active=True)[:6]
    recent_lessons = Lesson.objects.filter(is_active=True).order_by('-created_at')[:5]

    context = {
        'categories': categories,
        'recent_lessons': recent_lessons,
        'total_lessons': Lesson.objects.filter(is_active=True).count(),
        'total_cards': Card.objects.filter(is_active=True).count(),
    }
    return render(request, 'trening/home.html', context)


def categories_list(request):
    """Список всех тем"""
    categories = Category.objects.filter(is_active=True).annotate(
        lessons_count=Count('lessons', filter=models.Q(lessons__is_active=True))  # Теперь models.Q работает
    )

    context = {
        'categories': categories,
        'title': 'Все темы'
    }
    return render(request, 'trening/categories.html', context)


def category_detail(request, category_slug):
    """Детальная страница темы"""
    category = get_object_or_404(Category, slug=category_slug, is_active=True)
    lessons = category.lessons.filter(is_active=True)

    context = {
        'category': category,
        'lessons': lessons,
        'title': category.name
    }
    return render(request, 'trening/category_detail.html', context)


def lesson_detail(request, category_slug, lesson_slug):
    """Детальная страница урока"""
    category = get_object_or_404(Category, slug=category_slug, is_active=True)
    lesson = get_object_or_404(Lesson, slug=lesson_slug, category=category, is_active=True)

    # Получаем следующий и предыдущий уроки
    lessons = category.lessons.filter(is_active=True).order_by('order', 'created_at')
    lesson_list = list(lessons)
    current_index = lesson_list.index(lesson) if lesson in lesson_list else -1

    prev_lesson = lesson_list[current_index - 1] if current_index > 0 else None
    next_lesson = lesson_list[current_index + 1] if current_index < len(lesson_list) - 1 else None

    cards_count = lesson.cards.filter(is_active=True).count()

    context = {
        'category': category,
        'lesson': lesson,
        'prev_lesson': prev_lesson,
        'next_lesson': next_lesson,
        'cards_count': cards_count,
        'title': lesson.name
    }
    return render(request, 'trening/lesson_detail.html', context)


def cards_list(request):
    """Список всех карточек"""
    cards = Card.objects.filter(is_active=True).select_related('lesson', 'lesson__category')

    # Пагинация
    paginator = Paginator(cards, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'cards': page_obj,
        'title': 'Все карточки'
    }
    return render(request, 'trening/cards_list.html', context)


def lesson_cards(request, category_slug, lesson_slug):
    """Карточки конкретного урока"""
    category = get_object_or_404(Category, slug=category_slug, is_active=True)
    lesson = get_object_or_404(Lesson, slug=lesson_slug, category=category, is_active=True)
    cards = lesson.cards.filter(is_active=True)

    context = {
        'category': category,
        'lesson': lesson,
        'cards': cards,
        'title': f'Карточки: {lesson.name}'
    }
    return render(request, 'trening/karti.html', context)


def study_card(request, card_id):
    """Страница изучения карточки"""
    card = get_object_or_404(Card, id=card_id, is_active=True)

    # Получаем следующую карточку
    next_card = Card.objects.filter(
        lesson=card.lesson,
        is_active=True,
        order__gt=card.order
    ).order_by('order').first()

    if not next_card:
        next_card = Card.objects.filter(
            lesson=card.lesson,
            is_active=True,
            order__gt=0
        ).order_by('order').first()

    context = {
        'card': card,
        'next_card': next_card,
        'title': 'Изучение карточки'
    }
    return render(request, 'trening/study_card.html', context)


def quiz(request, lesson_id):
    """Тестирование по уроку"""
    lesson = get_object_or_404(Lesson, id=lesson_id, is_active=True)
    cards = lesson.cards.filter(is_active=True)

    if request.method == 'POST':
        # Обработка ответов
        score = 0
        total = len(cards)
        results = []

        for card in cards:
            user_answer = request.POST.get(f'answer_{card.id}', '')
            is_correct = user_answer.lower().strip() == card.answer.lower().strip()
            if is_correct:
                score += 1
            results.append({
                'card': card,
                'user_answer': user_answer,
                'is_correct': is_correct
            })

        context = {
            'lesson': lesson,
            'results': results,
            'score': score,
            'total': total,
            'percentage': (score / total * 100) if total > 0 else 0
        }
        return render(request, 'trening/quiz_results.html', context)

    context = {
        'lesson': lesson,
        'cards': cards,
        'title': f'Тест: {lesson.name}'
    }
    return render(request, 'trening/quiz.html', context)


def help_page(request):
    """Страница помощи"""
    return render(request, 'trening/help.html', {'title': 'Помощь'})
