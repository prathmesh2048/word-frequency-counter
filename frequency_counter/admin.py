from django.contrib import admin
from .models import Web_address, Results

class WebAddress(admin.ModelAdmin):
    list_display = ['url']
class ResultsView(admin.ModelAdmin):
    list_display = ['word','frequency','associated_url']

admin.site.register(Web_address, WebAddress)
admin.site.register(Results, ResultsView)