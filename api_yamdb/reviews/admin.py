from django.contrib import admin
from .models import Review, Comments, Titles, Categories, Genres


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


class GenresAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name')
    search_fields = ('slug',)
    empty_value_display = '-пусто-'


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name')
    search_fields = ('slug',)
    empty_value_display = '-пусто-'


class TitlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'category')
    search_fields = ('genre__slug', 'category__slug', 'year', 'name')
    list_editable = ('name', 'description', 'category')
    empty_value_display = '-пусто-'


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Genres, GenresAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Titles, TitlesAdmin)