from django.contrib import admin

from .models import Topic


class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    search_fields = ('title',)


admin.site.register(Topic, TopicAdmin)
