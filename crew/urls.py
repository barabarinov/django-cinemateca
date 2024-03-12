from django.urls import path

from crew.views import (
    DirectorDetailView,
    DirectorCreateView,
    DirectorUpdateView,
    DirectorDeleteView,
    ActorDetailView,
    ActorCreateView,
    ActorUpdateView,
    ActorDeleteView,
)

app_name = "crew"

urlpatterns = [
    path("director/<int:pk>/", DirectorDetailView.as_view(), name="director-detail"),
    path("director/create/", DirectorCreateView.as_view(), name="director-create"),
    path(
        "director/update/<int:pk>/",
        DirectorUpdateView.as_view(),
        name="director-update",
    ),
    path(
        "director/delete/<int:pk>/",
        DirectorDeleteView.as_view(),
        name="director-delete",
    ),
    path("actor/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),
    path("actor/create/", ActorCreateView.as_view(), name="actor-create"),
    path("actor/update/<int:pk>/", ActorUpdateView.as_view(), name="actor-update"),
    path("actor/delete/<int:pk>/", ActorDeleteView.as_view(), name="actor-delete"),
]
