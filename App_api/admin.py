from django.contrib import admin
from App_api.models import App_api

# Register your models here.
class App_apiAdmin(admin.ModelAdmin):
    list_display = ['sectionname','sectiondesc','sectionmaker','create_time','id']
    
admin.site.register(App_api)