from django.contrib import admin
from profiles.models import Profile, Skill, JobSeeker, Recruiter, AppliedJobs, SavedJobs


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "date_joined", "is_jobseeker", "is_recruiter"]
    readonly_fields = ("date_joined", "last_login", )
    fieldsets = (
        ("ANA BİLGİLER", {
            "fields": ("username", "password", "first_name", "last_name", "email", )
        }),
        ("GENEL BİLGİLER", {
            "fields": ("is_active", "is_jobseeker", "is_recruiter", "is_staff", "is_superuser", "groups",
                       "user_permissions", "date_joined", "last_login")
        })
    )

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


@admin.register(JobSeeker)
class JobSeekerAdmin(admin.ModelAdmin):
    list_display = ["email", "first_name", "last_name", "date_joined", "is_active"]
    list_editable = ("is_active",)
    readonly_fields = ("updated", "date_joined", "slug")
    # prepopulated_fields = {
    #     'slug': ('name', 'surname'),
    # }
    fieldsets = (
        ("ANA BİLGİLER", {
            "fields": ("profile", "first_name", "last_name", "slug")
        }),
        ("GENEL BİLGİLER", {
            "fields": ("is_active", "email", "phone", "country", "city", "avatar", "profession_title",
                       "skills", "short_resume", "cv_file", "updated", "date_joined", )
        })
    )

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


@admin.register(Recruiter)
class RecruiterAdmin(admin.ModelAdmin):
    list_display = ["email", "first_name", "last_name", "date_joined", "is_active"]
    list_editable = ("is_active",)
    readonly_fields = ("updated", "date_joined", "slug")
    # prepopulated_fields = {
    #     'slug': ('name', 'surname'),
    # }
    fieldsets = (
        ("ANA BİLGİLER", {
            "fields": ("profile", "first_name", "last_name", "slug")
        }),
        ("GENEL BİLGİLER", {
            "fields": ("is_active", "email", "phone", "country", "avatar", "profession_title",
                       "company", "updated", "date_joined", )
        })
    )

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


admin.site.register(Skill)
admin.site.register(SavedJobs)
admin.site.register(AppliedJobs)
