from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Address, Event, Image, Menu, MenuItem, Social

admin.site.register(Address)
admin.site.register(Social)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    exclude = ('events', )
    list_display = ('get_preview', )
    readonly_fields = ('get_large_preview', )

    def get_preview(self, obj):
        return mark_safe('<img style="width: 75px" src="{' + obj.image.url + '}"/>')
    get_preview.short_description = 'превью'

    def get_large_preview(self, obj):
        return mark_safe('<img src="{' + obj.image.url + '}"/>')
    get_preview.short_description = 'превью'


class ImageInline(admin.TabularInline):
    model = Image.events.through
    raw_id_fields = ('image', )
    readonly_fields = ('get_preview', )
    extra = 1

    def get_preview(self, obj):
        return mark_safe('<img style="width: 150px" src="{' + obj.image.image.url +'}"/>')
    get_preview.short_description = 'превью'


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    prepopulated_fields = {'slug': ('title', )}


class MenuInline(admin.TabularInline):
    model = MenuItem.menus.through
    extra = 1


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    inlines = [MenuInline]
    exclude = ('menus', )
    search_fields = ('title', )


class MenuItemInline(admin.TabularInline):
    model = MenuItem.menus.through
    autocomplete_fields = ('menuitem', )
    extra = 1
    verbose_name = 'Товар'
    verbose_name_plural = 'Товары'


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'event', )
    list_filter = ('event', )
    inlines = [MenuItemInline]
    search_fields = ('title', )
