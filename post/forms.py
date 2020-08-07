from ckeditor.widgets import CKEditorWidget
from django import forms

from post.models import Post


class PostForm(forms.Form):
    title = forms.CharField(label='Заголовок', max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': 'Введите название статьи'}))
    content = forms.CharField(widget=CKEditorWidget, label='Текст статьи')
    image = forms.ImageField(label='Изображение')
