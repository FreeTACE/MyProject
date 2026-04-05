from django.contrib import admin
from .models import Category, Lesson, Card

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['order', 'is_active']

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'order', 'is_active', 'created_at']
    list_filter = ['category', 'is_active', 'created_at']
    search_fields = ['name', 'description', 'content']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['order', 'is_active']
    filter_horizontal = []

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['question', 'lesson', 'order', 'is_active', 'created_at']
    list_filter = ['lesson', 'is_active', 'created_at']
    search_fields = ['question', 'answer', 'hint']
    list_editable = ['order', 'is_active']