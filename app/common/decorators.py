from django.http import HttpResponseBadRequest
import functools


def ajax_required(func):
    """Decorator that only allows ajax requests to have access"""

    @functools.wraps(func)
    def wrapper(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest
        return func(request, *args, **kwargs)

    return wrapper
