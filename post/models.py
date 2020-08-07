from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статья"

    def __str__(self):
        return self.title


    title = models.CharField(max_length=256)
    content = RichTextField()
    image = models.ImageField()
