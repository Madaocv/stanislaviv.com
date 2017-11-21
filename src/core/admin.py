# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
# Register your models here.
from .models import Event, Gategories,Partners
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('title','location', 'category', 'event_day', 'status','source','bar',)
    list_filter = ('status','event_day','source', 'category', 'publish')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    search_fields = ('title',)

    def bar(self, obj):  # receives the instance as an argument
        return '<img src="{thumb}" width="100"/>'.format(
            thumb=obj.photo.url,
        )
    bar.allow_tags = True
    bar.short_description = u'Постер'

class GategoriesAdmin(admin.ModelAdmin):
    list_display = ('title','id',)
admin.site.register(Event, EventAdmin)
#admin.site.register(Group)
admin.site.register(Partners)
admin.site.register(Gategories,GategoriesAdmin)