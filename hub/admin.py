from django.contrib import admin
from hub.models import Icon, Item, Character, Slot


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'character']
admin.site.register(Item, ItemAdmin)


class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner']
admin.site.register(Character, CharacterAdmin)


class SlotAdmin(admin.ModelAdmin):
    list_display = ['name', 'character']
admin.site.register(Slot, SlotAdmin)

admin.site.register(Icon)
