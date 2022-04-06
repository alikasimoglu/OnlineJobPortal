from django.core.exceptions import PermissionDenied


def user_is_jobseeker(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_jobseeker:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap


def user_is_recruiter(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_recruiter:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap
