from django.http import HttpResponse


# Create your views here.
def index(request):
	return HttpResponse("Sample6 Hello, world. You're at the quickstart index.")
