from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Asset, Portfolio, UserAsset


def index(request):
    return render(request, 'main/index.html')


def assets(request):
    assets = Asset.objects.order_by('short_name')
    context = {
        'assets': assets,
    }
    return render(request, 'main/assets.html', context)


class AssetCreateView(CreateView):
    model = Asset
    success_url = reverse_lazy('main:assets')
    template_name_suffix = '_create'
    fields = ('name', 'short_name', 'asset_type')


def portfolios(request):
    portfolios = Portfolio.objects.order_by('-date_added')
    context = {
        'portfolios': portfolios,
    }
    return render(request, 'main/portfolios.html', context)


def portfolio(request, pk):
    portfolio = Portfolio.objects.get(pk=pk)
    user_assets = portfolio.userasset_set.order_by('balance')
    context = {
        'portfolio': portfolio,
        'user_assets': user_assets,
    }
    return render(request, 'main/portfolio.html', context)


class PortfolioCreateView(CreateView):
    model = Portfolio
    success_url = reverse_lazy('main:portfolios')
    template_name_suffix = '_create'
    fields = ('name',)


class PortfolioDeleteView(DeleteView):
    model = Portfolio
    success_url = reverse_lazy('main:portfolios')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['portfolios'] = Portfolio.objects.all()
        return context


class PortfolioUpdateView(UpdateView):
    model = Portfolio
    success_url = reverse_lazy('main:portfolios')
    template_name_suffix = '_update'
    fields = ('name',)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['portfolios'] = Portfolio.objects.all()
        return context


class UserAssetCreateView(CreateView):
    model = UserAsset
    template_name_suffix = '_create'
    fields = ('asset', 'balance',)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.portfolio = Portfolio.objects.get(pk=self.kwargs['portfolio_pk'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse_lazy('main:portfolio', kwargs={'pk': self.kwargs['portfolio_pk']})

    # TODO: написать отлавливаение IntegrityError при создании актива, который уже есть.


class UserAssetDeleteView(DeleteView):
    model = UserAsset
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['userassets'] = UserAsset.objects.all()
        return context
    
    def get_success_url(self):
        return reverse_lazy('main:portfolio', kwargs={'pk': self.kwargs['portfolio_pk']})


class UserAssetUpdateView(UpdateView):
    model = UserAsset
    template_name_suffix = '_update'
    fields = ('asset', 'balance',)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['userassets'] = UserAsset.objects.all()
        return context
    
    def get_success_url(self):
        return reverse_lazy('main:portfolio', kwargs={'pk': self.kwargs['portfolio_pk']})
    