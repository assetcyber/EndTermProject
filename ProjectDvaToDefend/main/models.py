import email
from django import forms
from pyexpat import model
from django.db import models
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField

# Create your models here.
class Famous_Persons(models.Model):
    name = models.CharField('Имя', max_length=30)
    biography = models.TextField('Биография')
    author_of_publication = models.CharField('Имя автора публикации', max_length=30)
    slug = models.SlugField(unique=True, verbose_name='URL')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return f'/{self.id}'
        return reverse('post', kwargs = {'post_slug':self.slug})
        # это нужно после update

    class Meta:
        verbose_name = 'Знаменитый писатель'
        verbose_name_plural = 'Знаменитые писатели'

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    img = models.ImageField (height_field=100, width_field=100)
    
class Authentithication(models.Model):
    login = models.CharField('Логин', max_length=50)
    password = models.TextField('Пароль')
    
class Email(models.Model):
    email = models.EmailField("Электронная почта", max_length=254)

class Dopcont(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    img = models.ImageField (height_field=100, width_field=100)



