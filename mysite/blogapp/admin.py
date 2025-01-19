from django.contrib import admin
from .models import Article

@admin.register(Article)
class MainModel(admin.ModelAdmin):
    list_display = ('id', 'title', 'body_s',  'p_d')


    def body_s(self, obj):
        if len(obj.body) >= 51:
            return obj.body[:50]+'...'
        else:
            return obj.body
