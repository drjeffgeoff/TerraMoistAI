from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse


def login_required_custom(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('login'))
        return view_func(request, *args, **kwargs)
    return _wrapped_view

