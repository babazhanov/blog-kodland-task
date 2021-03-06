"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include

from blog import settings
from post.views import PostListView, PostDetailView, add_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name="post-list"),

    path('detail/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('add/', add_post, name="post-add"),

    re_path(r'^ajaximage/', include('ajaximage.urls')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
