from django.urls import path
from . import views

urlpatterns = [
    path('filtered_data/', views.filtered_data, name='filtered_data'),
    path('generate-excel/', views.generate_excel, name='generate_excel')
]
