from django.contrib import admin
from .models import Shop, Item

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc', 'address']
    list_play_links = ['name']
    search_fields = ['name']

    def desc(self, shop):
        return shop.content[:20] + "..."

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass

