from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Movie
# Create your views here.


class MovieListView(ListView):
    model = Movie
    ordering = ['-release_date']

    paginate_by = 6


class MovieDetailView(DetailView):
    model = Movie


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ['movie_name', 'description', 'poster_image', 'genre', 'language',
              'IMDB_rating', 'cast', 'carousal_pic1', 'carousal_pic2', 'carousal_pic3']

    def form_valid(self, form):
        form.instance.director = self.request.user
        return super().form_valid(form)


class MovieUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Movie
    fields = ['movie_name', 'description', 'poster_image', 'genre', 'language',
              'IMDB_rating', 'cast', 'carousal_pic1', 'carousal_pic2', 'carousal_pic3']

    def form_valid(self, form):
        form.instance.director = self.request.user
        return super().form_valid(form)

    def test_func(self):
        movie = self.get_object()
        if self.request.user == movie.director:
            return True
        return False


class MovieDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Movie
    fields = ['movie_name', 'description', 'poster_image', 'genre', 'language',
              'IMDB_rating', 'cast', 'carousal_pic1', 'carousal_pic2', 'carousal_pic3']

    success_url = reverse_lazy('movie_list')

    def test_func(self):
        movie = self.get_object()
        if self.request.user == movie.director:
            return True
        return False


class GenreListView(ListView):
    pass


# redirecting root to homepage '/movie'
def indexView(req):
    return redirect('movie/')
