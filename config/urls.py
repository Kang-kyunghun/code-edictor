from django.urls import path

from ui import ide
urlpatterns = [
        path("", ui.ide)
]
