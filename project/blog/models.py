from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(
        verbose_name="Заголовок",
        max_length=100,
    )
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    


class News(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="Кат",
        verbose_name="Кат",
        blank=True,
        null=True
    )
    title = models.CharField(
        verbose_name="Заголовок",
        max_length=100,
    )
    description = models.TextField(
        verbose_name="Оописание",
        blank=True,
        null=True,
        default="По умол.описание"
    )
    
    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"
    
    def __str__(self):
        return self.title


class NewsImage(models.Model):
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Новости"
    )
    image = models.ImageField(
        "Фото",
        upload_to="news/photos",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Фото новостей'
        verbose_name_plural = 'Фото новостей'
    
    def __str__(self):
        return f"Фото-{self.news.title}"

