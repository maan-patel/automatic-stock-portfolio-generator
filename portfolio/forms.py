from django import forms

from .models import Portfolio

class PortfolioForm(forms.ModelForm):
    stock_name = forms.CharField(required=True,
                                 widget=forms.TextInput(attrs={
                                     'placeholder': 'Stock Ticker',
                                     'class': 'email_boton',
                                 }))
    investment_value = forms.DecimalField(required=True,
                                          widget=forms.NumberInput(attrs={
                                              'placeholder': 'Investment Value',
                                              'class': 'email_boton',
                                          }))
    risk_profile = forms.CharField(required=True,
                                   widget=forms.TextInput(attrs={
                                       'placeholder': 'Risk Level(Low, Medium, High)',
                                       'class': 'email_boton',
                                   }))
    time = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={
                               'placeholder': "Period: '5y', '1y', '6m', '1m', '1w', '1d'",
                               'class': 'email_boton',
                           }))
    graph_type = forms.CharField(required=True,
                                 widget=forms.TextInput(attrs={
                                     'placeholder': 'Chart Type (candle, line)',
                                     'class': 'email_boton',
                                 }))
    class Meta:
        model = Portfolio
        fields = [
            'stock_name',
            'investment_value',
            'risk_profile',
            'time',
            'graph_type',
        ]


class RawPortfolioForm(forms.Form):
    stock_name = forms.CharField(required = True,
                                 widget = forms.TextInput(attrs={
                                     'placeholder': 'Stock Ticker',
                                     'class': 'email_boton',
                                 }))
    investment_value = forms.DecimalField(required = True,
                                 widget = forms.NumberInput(attrs={
                                     'placeholder': 'Investment Value',
                                     'class': 'email_boton',
                                 }))
    risk_profile = forms.CharField(required = True,
                                 widget = forms.TextInput(attrs={
                                     'placeholder': 'Risk Level(Low, Medium, High)',
                                     'class': 'email_boton',
                                 }))
    time = forms.CharField(required = True,
                                 widget = forms.TextInput(attrs={
                                     'placeholder': "Period: '5y', '1y', '6m', '1m', '1w', '1d'",
                                     'class': 'email_boton',
                                 }))
    graph_type = forms.CharField(required = True,
                                 widget = forms.TextInput(attrs={
                                     'placeholder': 'Chart Type (candle, line)',
                                     'class': 'email_boton',
                                 }))
