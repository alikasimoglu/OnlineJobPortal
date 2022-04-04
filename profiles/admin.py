from django.contrib import admin
from profiles.models import Profile, Skill, JobSeeker, Recruiter

admin.site.register(Profile)


@admin.register(JobSeeker)
class JobSeekerAdmin(admin.ModelAdmin):
    list_display = ["email", "first_name", "last_name", "date_joined", "is_active"]
    list_editable = ("is_active",)
    readonly_fields = ("updated", "date_joined", "slug")
    # prepopulated_fields = {
    #     'slug': ('name', 'surname'),
    # }
    fieldsets = (
        ("SEO AYARLARI", {
            "fields": ("first_name", "last_name", "slug")
        }),
        ("ICERIK", {
            "fields": ("is_active", "profile", "email", "phone", "country", "city", "avatar", "profession_title",
                       "skills", "short_resume", "cv_file", "updated", "date_joined", )
        })
    )

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


admin.site.register(Recruiter)
admin.site.register(Skill)
