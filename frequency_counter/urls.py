from django.urls import path
from .views import index,results
urlpatterns = [
    path('', index, name='index'),
    path('results/', results, name='results'),
]