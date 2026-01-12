from django.db import models
from django.utils import timezone
from user.models import User
from django.utils.translation import gettext_lazy as _ 
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Автор'))
    title = models.CharField(max_length=128, verbose_name=_('Заголовок поста'))
    content = models.TextField(verbose_name=_('Контент поста'))
    time_stamp = models.DateField(default=timezone.now, verbose_name=_('Дата создания поста'))
    edited = models.BooleanField(default=False, verbose_name=_('Редактирован ли?'))

    class Meta: 
        verbose_name = _('Пост')
        verbose_name_plural = _('Посты')

class PostAttachment(models.Model):
    name = models.CharField(verbose_name= 'Название файла', blank=True)
    file = models.FileField(upload_to='images/', verbose_name= 'Файл')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def save(self, *args, **kwargs):
        file_name = self.file.name.split('.')[0].capitalize()
        self.name = file_name
        super().save(*args, **kwargs)

class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    content = models.TextField(verbose_name='контент комментарий')
    time_stamp = models.TimeField(default=timezone.now, verbose_name='дата и время')
    edited = models.BooleanField(default=False, verbose_name='изменен ли пост?')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    pinned = models.BooleanField(default=False, verbose_name='прекреплен ли данный комментарий?')
        
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментраии'

    def __str__(self):
        return f'{self.post} : {self.content} {self.time_stamp}'

    

