from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from crew.forms import DirectorCreationForm
from crew.models import Director


class DirectorDetailView(LoginRequiredMixin, DetailView):
    model = Director


class DirectorCreateView(CreateView):
    model = Director
    form_class = DirectorCreationForm
    template_name = "crew/director_form.html"
    success_url = reverse_lazy("login")


class DirectorUpdateView(LoginRequiredMixin, UpdateView):
    model = Director


class DirectorDeleteView(LoginRequiredMixin, DeleteView):
    model = Director


class ActorDetailView(LoginRequiredMixin, DetailView):
    ...


class ActorCreateView(LoginRequiredMixin, CreateView):
    ...


class ActorUpdateView(LoginRequiredMixin, UpdateView):
    ...


class ActorDeleteView(LoginRequiredMixin, DeleteView):
    ...
