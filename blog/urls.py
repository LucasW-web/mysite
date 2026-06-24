from django.urls import path

from blog import post_view

urlpatterns = [
    path('', post_view.PostView.as_view(), name='home'),
]