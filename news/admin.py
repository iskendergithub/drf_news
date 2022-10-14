from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'date']


admin.site.register(News, NewsAdmin)