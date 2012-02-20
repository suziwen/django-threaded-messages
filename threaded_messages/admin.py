from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.models import User, Group
from threaded_messages.models import *


class MessagesInline(admin.TabularInline):
    model = Message
    fields = ['sender', 'sent_at', 'body']
    readonly_fields = ['sender', 'sent_at', 'body']
    ordering = ("-sent_at",)
    can_delete = False


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'sent_at','body')
    ordering = ('-sent_at',)
    search_fields = ('body', 'sender__first_name',
                     'sender__last_name', 'sender__username')
admin.site.register(Message, MessageAdmin)


class ThreadAdmin(admin.ModelAdmin):
    list_display = ('subject', 'creator', 'replied')
    ordering = ('sent_at',)
    search_fields = ('subject', 'creator__first_name',
                     'creator__last_name', 'creator__username')
    inlines = [MessagesInline]
admin.site.register(Thread, ThreadAdmin)


admin.site.register(Participant)
