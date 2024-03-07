from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from crew.forms import DirectorCreationForm
from crew.models import Director, Actor


class DirectorDetailView(LoginRequiredMixin, DetailView):
    model = Director


class DirectorCreateView(CreateView):
    model = Director
    form_class = DirectorCreationForm
    template_name = "crew/director_form.html"
    success_url = reverse_lazy("login")


class DirectorUpdateView(LoginRequiredMixin, UpdateView):
    model = Director
    form_class = DirectorCreationForm
    template_name = "crew/director_form.html"
    success_url = reverse_lazy("movie:movie-list")


class DirectorDeleteView(LoginRequiredMixin, DeleteView):
    model = Director
    success_url = reverse_lazy("movie:movie-list")


class ActorDetailView(LoginRequiredMixin, DetailView):
    model = Actor


class ActorCreateView(LoginRequiredMixin, CreateView):
    model = Actor
    success_url = reverse_lazy("movie:movie-list")
    fields = "__all__"


class ActorUpdateView(LoginRequiredMixin, UpdateView):
    model = Actor
    success_url = reverse_lazy("movie:movie-list")
    fields = "__all__"


class ActorDeleteView(LoginRequiredMixin, DeleteView):
    model = Actor
    success_url = reverse_lazy("movie:movie-list")
