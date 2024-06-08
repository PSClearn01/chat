from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
#     path('response', response, name='response'),
#     path('requests', requests, name='requests')
]