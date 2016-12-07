from django.conf.urls import url
from django.contrib import admin
from portal.views import Index, SignupView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(Index.as_view()), name="home"),
]
