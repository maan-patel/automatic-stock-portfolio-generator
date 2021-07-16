from django.shortcuts import redirect, render
from .models import Portfolio
from .forms import PortfolioForm, RawPortfolioForm
from .models import Portfolio
from .controller import *
import mpld3


def portfolio_create_view(request, *args, **kwargs):
    obj = Portfolio.objects.latest('id')
    valid_stock = is_valid_ticker(obj.stock_name)
    # valid_investment_value = is_number_of_stocks(obj.stock_name, obj.investment_value)
    valid_graph = is_valid_graph(obj.graph_type)

    if not valid_stock:
        obj.stock_name = 'AAPL'
    
    if not valid_graph:
        obj.graph_type = 'line'

    



    # if obj.graph_type.lower() :
    # obj.graph_type = 'Area'

    # if not valid_investment_value:
    #     obj.investment_value = 100000

    tickers = recommended_tickers(obj.stock_name)
    prices = recommended_stock_weight(obj.stock_name)
    graph = number_for_graph(obj.graph_type)
    # sentiment_average = sentiment_score(obj.stock_name)
    # sentiment_news_average = sentiment_for_news()
    # print(graph)
    context = {
        'obj': obj,
        'tickers': tickers,
        'prices' : prices,
        'graph': graph,
        # 'senti': sentiment_average,
        # 'senti_news': sentiment_news_average
    }
    # print(tickers)
    # print(obj.stock_name)
    # print(obj.investment_value)
    # print(obj.risk_profile)

    return render(request, 'portfolio/portfolio_create_view.html', context)


def portfolio_view(request, *args, **kwargs):
    obj = Portfolio.objects.latest('id')
    my_form = RawPortfolioForm()
    if request.method == 'POST':
        my_form = RawPortfolioForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Portfolio.objects.create(**my_form.cleaned_data)
            return redirect('/portfolio/')
        else:
            print(my_form.error)

    context = {
        'form': my_form,
        'obj': obj,
    }

    return render(request, 'portfolio/portfolio_view.html', context)
