from django.urls import include, re_path
from oauth import views as oauth_views

urlpatterns = [
    re_path(r"^$", oauth_views.index, name="evernote_index"),
    re_path(r"^auth/$", oauth_views.auth, name="evernote_auth"),
    re_path(r"^callback/$", oauth_views.callback, name="evernote_callback"),
    re_path(r"^reset/$", oauth_views.reset, name="evernote_auth_reset"),
]