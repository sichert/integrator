from django.contrib import admin

from openproject_sync.models import WorkPackage, TimeEntry, Project


class ProjectAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return False


class WorkPackageAdmin(admin.ModelAdmin):
    list_display = ("subject", "project")
    list_filter = ("project",)

    def get_readonly_fields(self, request, obj=None):
        return (
            "createdAt",
            "updatedAt",
            "derivedStartDate",
            "derivedDueDate",
            "derivedPercentageDone",
            "derivedEstimatedTime",
            "derivedRemainingTime",
        )

    def has_add_permission(self, request, obj=None):
        return False


class TimeEntryAdmin(admin.ModelAdmin):
    list_display = ("work_package", "comment", "spentOn", "hours")
    list_filter = ("work_package",)

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(Project, ProjectAdmin)
admin.site.register(WorkPackage, WorkPackageAdmin)
admin.site.register(TimeEntry, TimeEntryAdmin)
