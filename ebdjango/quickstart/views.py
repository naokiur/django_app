from django.http import HttpResponse


# Create your views here.
def index(request):
	return HttpResponse("Sample4 Hello, world. You're at the quickstart index.")
