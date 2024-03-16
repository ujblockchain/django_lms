from django.urls import path

from . import views

urlpatterns = [
    path("", views.contactus),
    path("message-sent", views.messageSent),
]
