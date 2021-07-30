from django.contrib import admin

from .models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',
                    'list_date', 'cater')
    list_display_links = ('id', 'title')
    list_filter = ('cater',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address',
                     'city', 'state', 'zipcode')
    list_per_page = 25


admin.site.register(Entry, EntryAdmin)
