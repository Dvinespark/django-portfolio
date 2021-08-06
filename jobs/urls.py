from django.urls import path
from .views import *

urlpatterns = [
	path('', index, name='index'),
	path('<int:pk>', job_detail, name='job_detail'),
]