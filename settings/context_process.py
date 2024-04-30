from .models import Settings

def context_process(request):
    data=Settings.objects.last()
    return {'setting_data':data}