from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    ordering = ['id']
    search_fields = ['title', 'author_name']
    list_display = (
        'id',
        'title',
        'link',
        'creation_date',
        'amount_of_upvotes',
        'author_name',
    )
    list_display_links = (
        'id',
        'title',
    )


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    ordering = ['id']
    search_fields = ['author_name']
    list_display = (
        'id',
        'post',
        'author_name',
        'content',
        'creation_date',
    )
    list_display_links = (
        'id',
        'post',
    )
    raw_id_fields = ('post',)
