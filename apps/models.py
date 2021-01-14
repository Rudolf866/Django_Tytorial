from django.db import models

# Create your models here.
from django.forms import DateField
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()


class Company(models.Model):
    name = models.CharField(max_length=30, verbose_name="Компания")


class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Товар")
    name = models.CharField(max_length=30)
    price = models.IntegerField()


class Course(models.Model):
    name = models.CharField(max_length=30, verbose_name="Курс")


class Student(models.Model):
    name = models.CharField(max_length=30, verbose_name="Студент")
    courses = models.ManyToManyField(Course)


# class User(models.Model):
# name = models.CharField(max_length=20)

#
# class Account(models.Model):
#     login = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()  # Менеджер по умолчанию.
    published = PublishedManager()  # Наш новый менеджер.

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('apps:post_detail', args=[self.publish.year,
                                                 self.publish.month, self.publish.day, self.slug])
