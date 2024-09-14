from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

# Use include() to add URLS from the catalog application and authentication system
from django.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += [
    path("shop/", include("shop.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
