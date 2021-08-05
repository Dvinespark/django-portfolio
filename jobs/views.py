from django.shortcuts import render, HttpResponse
from .models import Job

# Create your views here.
def index(request):
	jobs = Job.objects.all()
	return render(request, 'jobs/home.html', {'jobs':jobs})
	