from django.urls import path
from .views import searcher, exercise, getResults

app_name = 'exercises'

urlpatterns = [
    path('', searcher, name='searcher'),
    path('<int:pk>/', exercise, name='exercise'),
    path('getresults/', getResults, name='getresults'),
]
