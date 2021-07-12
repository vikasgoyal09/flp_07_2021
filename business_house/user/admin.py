from django.contrib import admin
from . import models

# Register your models here.
# class WalletAdmin(admin.ModelAdmin):
#     readonly_fields = ('user_id', 'credit')
#     fields = ('user_id', 'credit')

admin.site.register(models.Wallet)
