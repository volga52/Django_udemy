from django.urls import path
import mainapp.views as mainapp

# Обязательная опция указание приложения
app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.accommodations, name='index'),
    # '' - указывает на отсутствие знаков в адресе после
    # перехода по ссылке в данный urls
    path('accommodation_details/<int:pk>/', mainapp.accommodation,
         name='accommodation'),
]
