from django.contrib import admin

from .forms import StatusForm
from .models import Status


class StatusAdmin(admin.ModelAdmin):
    list_display = ['user', '__str__', 'image']
    form=StatusForm
    #class Meta:
    #    model = StatusForm


admin.site.register(Status, StatusAdmin)
