from django.urls import path

from . import views
# create a new list urlpatterns file


urlpatterns = [
    path("january/", views.index, name="index")
    # Add more paths as needed
]
