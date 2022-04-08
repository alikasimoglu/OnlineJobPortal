from django.core.exceptions import PermissionDenied


def user_is_jobseeker(function):  # If the user is not the jobseeker, it will show the 403 error page.
    def wrap(request, *args, **kwargs):
        if request.user.is_active and request.user.is_jobseeker:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap


def user_is_recruiter(function):  # If the user is not the recruiter, it will show the 403 error page.
    def wrap(request, *args, **kwargs):
        if request.user.is_active and request.user.is_recruiter:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap
