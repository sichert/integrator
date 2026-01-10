from django.contrib import admin
from openproject_sync.models import WorkPackage, TimeEntry

admin.site.register(WorkPackage)
admin.site.register(TimeEntry)