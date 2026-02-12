from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),          # ← главная страница = каталог
    path('catalog/', views.catalog, name='catalog-alt'),  # ← можно оставить и старый путь
    path('catalog/<slug:slug>/', views.phone_detail, name='phone_detail'),
]