from django.apps import AppConfig


class RestaurantsConfig(AppConfig):
    name = 'restaurants'
    
    def home(request):
    	context = {
        "msg": "Hello World!"}
    	return render(request, 'template1.html',context)