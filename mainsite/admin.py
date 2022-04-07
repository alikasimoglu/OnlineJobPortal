from django.contrib import admin

from mainsite.models.applicants import Applicants
from mainsite.models.jobs import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ["job_title", "recruiter", "company", "date_added", "is_active"]
    list_editable = ("is_active",)
    readonly_fields = ("updated", "date_added", "slug")
    fieldsets = (
        ("ANA BİLGİLER", {
            "fields": ("job_title", "company", "recruiter", "slug")
        }),
        ("GENEL BİLGİLER", {
            "fields": ("is_active", "location", "skills_req", "job_insight", "description", "updated", "date_added", )
        })
    )

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


@admin.register(Applicants)
class ApplicantsAdmin(admin.ModelAdmin):
    list_display = ["applicant", "job", "date_posted"]
    readonly_fields = ("date_posted", )
    fieldsets = (
        ("ANA BİLGİLER", {
            "fields": ("applicant", "job")
        }),
        ("GENEL BİLGİLER", {
            "fields": ("date_posted", )
        })
    )

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True
