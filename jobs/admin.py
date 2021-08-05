from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered
# Register your models here.

job_models = apps.get_app_config('jobs').get_models()

for model in job_models:
	try:
		admin.site.register(model)
	except AlreadyRegistered:
		pass