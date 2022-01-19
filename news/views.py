# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.core.paginator import Paginator

from .models import Post
from .filters import NewsFilter
from .forms import PostForm

from datetime import datetime


class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['length'] = Post.objects.count()
        return context


class SearchNews(ListView):
    model = Post
    template_name = 'news_search.html'
    context_object_name = 'news_search'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context


class NewsDetail(DetailView):
    template_name = 'news_detail.html'
    queryset = Post.objects.all()


class AddNews(CreateView):
    template_name = 'news_add.html'
    context_object_name = 'news_add'
    form_class = PostForm


class UpdateNews(UpdateView):
    template_name = 'news_add.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class DeleteNews(DeleteView):
    template_name = 'news_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
