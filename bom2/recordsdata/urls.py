# urls.py
from django.urls import path
from . import views
from .views import get_equipment_data
from .views import filter_data


urlpatterns = [
    path('', views.home, name='home'),  # Handle root URL
    path('form/<str:equipment_type>/', views.equipment_form_view, name='equipment_form'),
    path('success/', views.success_page, name='success.html'),
    path('add-data/', views.add_data_view, name='add_data'),
    path('get-equipment-data/', views.get_equipment_data, name='get_equipment_data'),
      path('', filter_data, name='filter_data'),
]


