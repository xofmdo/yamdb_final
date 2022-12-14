from django.contrib import admin
from reviews.models import Comment, Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Страница отзывов в админке"""

    list_display = (
        'pk',
        'title',
        'text',
        'author',
        'pub_date',
        'score',
    )
    search_fields = ('text',)
    list_filter = ('pub_date', 'score', 'text',)
    empty_value_display = '-пусто-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Страница комментариев в админке"""

    list_display = (
        'pk',
        'review',
        'author',
        'text',
        'pub_date'
    )

    search_fields = (
        'text',
        'author'
    )
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
