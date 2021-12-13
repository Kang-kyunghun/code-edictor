from django.urls import path, include

urlpatterns = [
    path("ide", include('ide.urls'))
]
