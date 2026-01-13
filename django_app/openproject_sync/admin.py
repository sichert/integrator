from django.contrib import admin
from openproject_sync.models import WorkPackage, TimeEntry, Project


admin.site.register(Project)
admin.site.register(WorkPackage)
admin.site.register(TimeEntry)