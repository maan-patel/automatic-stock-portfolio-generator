from django.db import models


class Portfolio(models.Model):
    stock_name = models.CharField(max_length=10)
    investment_value = models.DecimalField(decimal_places=2, max_digits=1000000000)
    risk_profile = models.CharField(max_length = 30)
    time = models.CharField(max_length = 5)
    graph_type = models.CharField(max_length = 10)
