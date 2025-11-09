from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    bio = models.TextField(blank=True, verbose_name="Биография")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название жанра")
    description = models.TextField(blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        ordering = ['name']

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название книги")
    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='books',
        verbose_name="Автор"
    )
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")
    publication_year = models.IntegerField(verbose_name="Год публикации")
    genres = models.CharField(max_length=200, verbose_name="Жанры")
    co_authors = models.CharField(max_length=200, blank=True, verbose_name="Соавторы")
    summary = models.TextField(blank=True, verbose_name="Краткое описание")

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['title']

    def __str__(self):
        return self.title
