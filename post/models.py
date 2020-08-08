from ckeditor.fields import RichTextField
from django.db import models

from ajaximage.fields import AjaxImageField


class Post(models.Model):
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статья"

    def __str__(self):
        return self.title

    title = models.CharField(max_length=256)
    content = RichTextField()
    image = AjaxImageField(upload_to='uploads',
                           max_height=200,  # optional
                           max_width=200,  # optional
                           crop=True,  # optional
                           null=True,
                           blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_image(self):
        if self.image and self.image.url and len(self.image.url) > 0:
            return self.image.url
        else:
            return '/media/robot.png'
