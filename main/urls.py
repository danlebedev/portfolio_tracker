from django.urls import path

from . import views


app_name = 'main'
urlpatterns = [
    # Homepage.
    path('', views.index, name='index'),
    path('assets/', views.assets, name='assets'),
    path('portfolios/', views.portfolios, name='portfolios'),
]