from django.contrib import admin
from hub.models import Icon, Item, Character


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'character']
admin.site.register(Item, ItemAdmin)


class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner']
admin.site.register(Character, CharacterAdmin)

admin.site.register(Icon)
