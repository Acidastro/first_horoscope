from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='horoscope-index'),
    path('beautiful_table', views.beautiful_table),
    path('types', views.types),
    path('types/<value>', views.get_info_types, name='types-name'),
    path('<int:value>', views.get_info_horoscope_int),
    path('<str:value>', views.get_info_horoscope, name='horoscope-name'),


]
