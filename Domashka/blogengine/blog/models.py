from django.db import models
from django.shortcuts import reverse

# Create your models here.

#Здесь пишу модель пост, для создания постов блога
class POST(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    #slug = models.SlugField(max_length=150, unique=True) # Удобный уникальный url
    body = models.TextField(blank=True, db_index=True) #может быть пустым
    date_pub = models.DateTimeField(auto_now_add=True) #записываем дату публикации

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'id': self.id})

    def __str__(self): #переопределяю метод класса, чтобы в консоле удобно возвращались данные
        return '{}'.format(self.title)



