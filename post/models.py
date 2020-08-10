from ckeditor.fields import RichTextField
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.db import models

from ajaximage.fields import AjaxImageField


class Post(models.Model):
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статья"
        ordering = ['id']

    def __str__(self):
        return self.title

    title = models.CharField(max_length=256)
    content = RichTextField()
    image = AjaxImageField(upload_to='uploads',
                           default="robot.png",
                           null=True,
                           blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_image(self):
        if self.image and self.image.url and len(self.image.url) > 0:
            return self.image.url
        else:
            return static('uploads/robot.png')
