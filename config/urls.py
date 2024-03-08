from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include, reverse_lazy

from config import settings

urlpatterns = [
    path(
        "", lambda request: redirect(reverse_lazy("movie:movie-list"), permanent=True)
    ),
    path("movies/", include("movie.urls")),
    path("crew/", include("crew.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
