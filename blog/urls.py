from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:blog_id>', views.detail, name='detail'),
    path('new/', views.blogpost, name='new'),
    path('delete/<int:blog_id>/',views.delete,name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
