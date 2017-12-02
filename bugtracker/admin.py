# coding: utf-8
from django.contrib import admin
from .models import Ticket
from .models import Status
from .models import Project


class TicketAdmin(admin.ModelAdmin):
    list_display = ('status', 'title', 'project', 'text', 'created', 'user')
    list_filter = ['created', 'status', 'project']
    search_fields = ['title', 'text']


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ['title']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ['title']

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Project, ProjectAdmin)
