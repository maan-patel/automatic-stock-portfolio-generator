from django.shortcuts import render
from .models import Portfolio
from .forms import PortfolioForm, RawPortfolioForm
from .models import Portfolio
from .controller import recommended_tickers, recommended_stock_weight, is_valid_ticker, number_of_stocks
import mpld3


def portfolio_create_view(request, *args, **kwargs):
    obj = Portfolio.objects.latest('id')
    valid = is_valid_ticker(obj.stock_name)
    if not valid:
        obj.stock_name = 'AAPL'
    tickers = recommended_tickers(obj.stock_name)
    prices = recommended_stock_weight(obj.stock_name)

    context = {
        'obj': obj,
        'tickers': tickers,
        'prices' : prices,
        

    }
    print(tickers)
    print(obj.stock_name)
    print(obj.investment_value)
    print(obj.risk_profile)

    return render(request, 'portfolio/portfolio_create_view.html', context)


def portfolio_view(request, *args, **kwargs):
    obj = Portfolio.objects.latest('id')
    my_form = RawPortfolioForm()
    if request.method == 'POST':
        my_form = RawPortfolioForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Portfolio.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.error)

    context = {
        'form': my_form,
        'obj': obj,
    }

    return render(request, 'portfolio/portfolio_view.html', context)
