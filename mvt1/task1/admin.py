from django.contrib import admin
from .models import Buyer, Pipl

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')
    search_fields = ('name', )
    list_filter = ('balance', 'age', )
    fields = [('name', 'balance', 'age')]

@admin.register(Pipl)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size', 'age_limited')
    search_fields = ('title', )
    list_filter = ('cost', 'size', 'age_limited', )
    fieldsets = (
        ('Game Info', {
            'fields': (('title', 'cost'), )
        }),
        ('Game Description', {
            'fields': ('description', ('size', 'age_limited'),)
        }),
    )
