from django.contrib import admin
from .models import Post, PostAttachment, Comments
from django.utils.translation import gettext_lazy as _ 
# Register your models here.
# admin.site.register(Post)
# admin.site.register(PostAttachment)
# admin.site.register(Comments)

@admin.register(Post)
class CustomPostAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Автор'), {'fields': ('author',)}),
        (_('Оснавная информация поста (ru)'), {'fields': ('title_ru', 'content_ru')}),
        (_('Оснавная информация поста (en)'), {'fields': ('title_en', 'content_en')}),
        (_('Дополнительная информация поста'), {'fields': ('time_stamp', 'edited')})
    )
    add_fieldsets = (
        (_('Автор'), {'fields': ('author',)}),
        (_('Оснавная информация поста (ru)'), {'fields': ('title_ru', 'content_ru')}),
        (_('Оснавная информация поста (en)'), {'fields': ('title_en', 'content_en')}),
        )

    list_display = ('title', 'time_stamp', 'edited')
    search_fields = ('title', 'content', 'author__username') #пойск
    ordering = ('title', 'time_stamp') #сортировка

    def get_fieldsets(self, request, obj=None):
        if obj:
            return self.fieldsets
        return self.add_fieldsets

@admin.register(PostAttachment)
class CustomPostAttachment(admin.ModelAdmin):
    list_display=('name','file', 'post') 
    search_fields=('name','post__title')
    ordering=('post__title', 'name') 
    
    fieldsets=(
        ('На какой пост прекрепить', {'fields':('post',)}),
        ('Данные файла', {'fields': ('name','file')}),
    )


@admin.register(Comments)
class CustomCommentsAdmin(admin.ModelAdmin):
    list_display=('content','post','time_stamp','edited','pinned')
    search_fields=('content','author__username')
    ordering=('-time_stamp',)

    fieldsets = (
        ('Автор', {'fields': ('author',)}),
        ('пост и контент', {'fields': ('post', 'content')}),
        ('изменен / прикеплен', {'fields': ('pinned', 'edited')}),
    )
    add_fieldsets = (
        ('Автор', {'fields': ('author',)}),
        ('Создание Комментария', {'fields': ('post', 'content', 'pinned')}),
    )
    def get_fieldsets(self, request, obj=None):
        if obj:
            return self.fieldsets
        return self.add_fieldsets
    
