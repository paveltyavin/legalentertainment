from urllib.parse import urljoin

from django.conf import settings
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from app.models import Document, Client, Article


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['client_list'] = Client.objects.all()
        result['article_list'] = Article.objects.all()[:2]
        try:
            d = Document.objects.get(slug='price')
            result['price_url'] = urljoin(settings.MEDIA_URL, d.file.url)
        except Document.DoesNotExist:
            pass
        return result


class ArticleDetailView(DetailView):
    queryset = Article.objects.all()
    template_name = 'article_detail.html'


class ArticleListView(ListView):
    queryset = Article.objects.all()
    template_name = 'article_list.html'
