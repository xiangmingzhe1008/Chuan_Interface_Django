from django.shortcuts import render
from App_api.models import App_api

# Create your views here.
def section_manage(request):
    username = request.session.get('user','')
    section_list = App_api.objects.all()
    return render(request,"App_api_manage.html",{"user":username,"sections":section_list})
