from django.shortcuts import render
from .models import Asset, Portfolio


def index(request):
    return render(request, 'main/index.html')


def assets(request):
    assets = Asset.objects.order_by('short_name')
    context = {
        'assets': assets,
    }
    return render(request, 'main/assets.html', context)


def portfolios(request):
    portfolios = Portfolio.objects.order_by('-date_added')
    context = {
        'portfolios': portfolios,
    }
    return render(request, 'main/portfolios.html', context)
