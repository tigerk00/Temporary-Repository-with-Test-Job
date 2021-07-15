from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from register.views import register
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#Settings of Schema
schema_view = get_schema_view(
    openapi.Info(
        title="Pokemon Site API",
        default_version="v1",
        description="A sample API for getting info about players and their pokemons",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="kostia.lagoda@gmail.com"),
        license=openapi.License(name="BSD License"),
        ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    )

# remove annoying sidebar from admin-panel
admin.autodiscover()
admin.site.enable_nav_sidebar = False


# My apps, api, admin panel
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pokemon_world/', include("pokemon.urls")),
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api-doc-swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]


# Register, Login, Logout, etc...
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/register", register , name="register"),
]

# Static, Media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
