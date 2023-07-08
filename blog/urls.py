from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<int:blog_id>/', views.blog, name='blog'),
    path('create/', views.createblog, name='createblog'),
    path('category/<str:query>/', views.category, name='category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
