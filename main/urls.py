from django.urls import path
from . import views
urlpatterns=[path("shorten",views.shorten,name="shorten"),
             path("<str:short_url>",views.go,name="go")
             ]