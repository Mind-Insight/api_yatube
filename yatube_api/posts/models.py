from django.contrib.auth import get_user_model
from django.db import models

from api.constants import MAX_TEXT_LENGTH

User = get_user_model()


class Group(models.Model):
    title = models.CharField("Название", max_length=200)
    slug = models.SlugField("Слаг", unique=True)
    description = models.TextField("Описание")

    def __str__(self):
        return self.title[:MAX_TEXT_LENGTH]


class Post(models.Model):
    text = models.TextField("Текст")
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="автор",
    )
    image = models.ImageField(
        "Изображение", upload_to="posts/", null=True, blank=True
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Группа",
    )

    class Meta:
        default_related_name = "posts"

    def __str__(self):
        return self.text[:MAX_TEXT_LENGTH]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Автор",
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Пост",
    )
    text = models.TextField("Текст")
    created = models.DateTimeField(
        "Дата добавления", auto_now_add=True, db_index=True
    )

    def __str__(self):
        return self.text[:MAX_TEXT_LENGTH]
