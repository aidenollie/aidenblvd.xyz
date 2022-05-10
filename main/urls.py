from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
path("", views.home, name="home"),
path("home/", views.home, name="home"),
path("contact", views.contact, name="contact"),
]

urlpatterns += staticfiles_urlpatterns()