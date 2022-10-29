from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title='Music Catalog',
        default_version='v0',
        description='There is no description yet.',
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('readoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
