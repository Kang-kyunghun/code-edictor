from django.urls import path, include

from core.views import ping
urlpatterns = [
    path("ping", ping),
    path("ide", include('ide.urls'))
]
