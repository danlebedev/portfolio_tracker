from django.urls import path

from . import views


app_name = 'main'
urlpatterns = [
    # Homepage.
    path('', views.index, name='index'),
    path('assets/', views.assets, name='assets'),
    path('portfolios/', views.portfolios, name='portfolios'),
    path(
        'portfolios/add/',
        views.PortfolioCreateView.as_view(),
        name='portfolio_add'
    ),
    path('portfolios/<int:pk>/', views.portfolio, name='portfolio'),
    path(
        'portfolios/<int:pk>/delete/',
        views.PortfolioDeleteView.as_view(),
        name='portfolio_delete'
    ),
    path(
        'portfolios/<int:pk>/update/',
        views.PortfolioUpdateView.as_view(),
        name='portfolio_update',
    )
]