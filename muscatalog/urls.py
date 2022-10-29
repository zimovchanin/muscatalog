from django.contrib import admin
from django.urls import path, include

from .yasg import urlpatterns as yasg_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('music/api/v0/', include('music.api.v0.urls')),
]

urlpatterns += yasg_urlpatterns
