from django.contrib import admin
from django.urls import path

from promedio import views as p_views
from apiTest.api_view import UserAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('promedio/', p_views.index),
    path('api/users/make', UserAPI.as_view())
]
