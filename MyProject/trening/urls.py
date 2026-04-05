from django.urls import path
from . import views

app_name = 'trening'

urlpatterns = [
    # Главная страница
    path('', views.home, name='home'),

    # Категории/Темы
    path('categories/', views.categories_list, name='categories_list'),
    path('category/<slug:category_slug>/', views.category_detail, name='category_detail'),

    # Уроки
    path('category/<slug:category_slug>/lesson/<slug:lesson_slug>/',
         views.lesson_detail, name='lesson_detail'),

    # Карточки
    path('cards/', views.cards_list, name='cards_list'),
    path('category/<slug:category_slug>/lesson/<slug:lesson_slug>/cards/',
         views.lesson_cards, name='lesson_cards'),
    path('cards/study/<int:card_id>/', views.study_card, name='study_card'),
    path('cards/quiz/<int:lesson_id>/', views.quiz, name='quiz'),

    # Помощь
    path('help/', views.help_page, name='help'),
]