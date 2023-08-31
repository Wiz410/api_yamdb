from django.contrib import admin
from .models import Review, Comments


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'score', 'pub_date', 'title')
    search_fields = ('text',)
    list_filter = ('text',)
    list_editable = ('author', 'text', 'score', 'title')
    empty_value_display = '-пусто-'


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'pub_date', 'review')
    search_fields = ('text',)
    list_filter = ('text',)
    list_editable = ('author', 'text', 'review')
    empty_value_display = '-пусто-'


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comments, CommentsAdmin)
