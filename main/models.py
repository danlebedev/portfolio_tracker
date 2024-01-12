from django.db import models


class Asset(models.Model):
    name = models.CharField(max_length=20)
    short_name = models.CharField(max_length=10)
    CHOICES = (
        ('1', 'currency'),
        ('2', 'cryptocurrency'),
    )
    asset_type = models.CharField(
        max_length=1,
        choices=CHOICES,
        default='1',
    )


class Portfolio(models.Model):
    name = models.CharField(max_length=20)
