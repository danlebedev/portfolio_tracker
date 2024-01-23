from django.urls import path

from . import views


app_name = 'main'
urlpatterns = [
    # Homepage.
    path('', views.index, name='index'),
    # Assets.
    path('assets/', views.assets, name='assets'),
    path(
        'assets/create/',
        views.AssetCreateView.as_view(),
        name='asset_create',
    ),
    path(
        'assets/<int:pk>/delete/',
        views.AssetDeleteView.as_view(),
        name='asset_delete',
    ),
    path(
        'assets/<int:pk>/update/',
        views.AssetUpdateView.as_view(),
        name='asset_update',
    ),
    # Portfolios.
    path('portfolios/', views.portfolios, name='portfolios'),
    path(
        'portfolios/create/',
        views.PortfolioCreateView.as_view(),
        name='portfolio_create'
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
    ),
    # Userassets.
    path(
        '<int:portfolio_pk>/userassets/create/',
        views.UserAssetCreateView.as_view(),
        name='userasset_create'
    ),
    path(
        '<int:portfolio_pk>/userassets/<int:pk>/delete/',
        views.UserAssetDeleteView.as_view(),
        name='userasset_delete'
    ),
    path(
        '<int:portfolio_pk>/userassets/<int:pk>/update/',
        views.UserAssetUpdateView.as_view(),
        name='userasset_update'
    ),
]