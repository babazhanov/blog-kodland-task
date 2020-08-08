from ckeditor.widgets import CKEditorWidget
from django import forms

from ajaximage.widgets import AjaxImageWidget


class PostForm(forms.Form):
    class Meta:
        exclude = ('image',)

    title = forms.CharField(label='Заголовок', max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': 'Введите название статьи'}))
    content = forms.CharField(widget=CKEditorWidget, label='Текст статьи')
    image = forms.CharField(widget=AjaxImageWidget(upload_to='uploads'), required=False)
