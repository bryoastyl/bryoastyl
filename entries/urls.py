from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='entries'),
    path('<int:entry_id>', views.entry, name='entry'),
    path('search', views.search, name='search'),
]
