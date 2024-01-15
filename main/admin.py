from django.contrib import admin

from . import models


admin.site.register(models.Asset)
admin.site.register(models.Portfolio)
admin.site.register(models.UserAsset)