from django.contrib import admin

from .models import Topic


class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'show_home',)
    search_fields = ('title',)


admin.site.register(Topic, TopicAdmin)
