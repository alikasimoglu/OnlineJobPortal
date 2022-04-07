from django import template
from mainsite.models.applicants import Applicants

register = template.Library()


@register.simple_tag(name="is_already_applied")
def is_already_applied(job, user):
    applied = Applicants.objects.filter(job=job, applicant=user)
    if applied:
        return True
    else:
        return False
