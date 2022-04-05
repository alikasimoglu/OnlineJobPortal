from django.contrib import admin

from mainsite.models.applicants import Applicants
from mainsite.models.jobs import Job
from mainsite.models.selected_applicants import Selected


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ["job_title", "recruiter", "company", "date_added", "is_active"]
    list_editable = ("is_active",)
    readonly_fields = ("updated", "date_added", "slug")
    # prepopulated_fields = {
    #     'slug': ('name', 'surname'),
    # }
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


admin.site.register(Applicants)
admin.site.register(Selected)
