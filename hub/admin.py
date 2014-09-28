from django.contrib import admin
from hub.models import Icon, Item, Character, Slot


class SlotAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Slot, SlotAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Item, ItemAdmin)


class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner']
admin.site.register(Character, CharacterAdmin)

admin.site.register(Icon)
