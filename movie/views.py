from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView,
)
from django.db.models import QuerySet

from movie.forms import MovieForm
from movie.models import Movie


class MovieListView(LoginRequiredMixin, ListView):
    model = Movie
    ordering = ["-year"]
    paginate_by = 8

    def get_queryset(self) -> QuerySet[Movie]:
        queryset = Movie.objects.all()

        if "year" in self.request.GET:
            return queryset.filter(year=self.request.GET.get("year"))
        if "genre" in self.request.GET:
            return queryset.filter(genre=self.request.GET.get("genres"))
        if "country" in self.request.GET:
            return queryset.filter(country__name=self.request.GET.get("countries"))

        return queryset.order_by("-year")


class MovieDetailView(LoginRequiredMixin, DetailView):
    model = Movie
    queryset = (
        Movie.objects.all()
        .select_related("director")
        .prefetch_related("actors", "countries", "genres")
    )


class MovieCreateView(LoginRequiredMixin, CreateView):
    form_class = MovieForm
    template_name = "movie/movie_form.html"
    success_url = reverse_lazy("movie:movie-list")


class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = "movie/movie_form.html"
    success_url = reverse_lazy("movie:movie-list")


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    template_name = "movie/movie_confirm_delete.html"
    success_url = reverse_lazy("movie:movie-list")
