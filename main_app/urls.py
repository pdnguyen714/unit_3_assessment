from django.urls import path
from . import views

urlpatterns = [
    path('', views.items_index, name='index'),
    path('add', views.ItemCreate.as_view(), name='item_create'),
    path('<int:pk>/delete', views.ItemDelete.as_view(), name='item_delete'),
]