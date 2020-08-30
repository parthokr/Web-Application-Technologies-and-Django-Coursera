from django.http import HttpResponse

def home(request):
	# add your individual unique string into the response
    return HttpResponse("Hello, world. 007d4a12 is the polls index.") 
