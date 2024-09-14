from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


urlpatterns = [
    path("admin/", admin.site.urls),
    path("shop/", include("shop.urls")),
]

urlpatterns += [
    path("", lambda request: redirect("shop/", permanent=True)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
