from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('add', views.add, name='add'),
    path('balance', views.balance, name='balance'),
    path('custom', views.balance_custom, name='custom'),
    path('results', views.results, name='results')
]