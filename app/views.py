from urllib.parse import urljoin

from django.conf import settings
from django.utils.translation import get_language
from django.views.generic.base import TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from app.models import Document, Client, Article, Promo


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['promo_list'] = Promo.objects.filter(is_active=True)
        result['client_list'] = Client.objects.all()
        result['article_list'] = Article.objects.all()[:2]
        try:
            d = Document.objects.get(slug='price')
            language = get_language()
            file_field = getattr(d, 'file_{}'.format(language), None)
            if file_field:
                result['price_url'] = urljoin(settings.MEDIA_URL, file_field.url)
        except Document.DoesNotExist:
            pass
        return result


class ArticleDetailView(DetailView):
    queryset = Article.objects.all()
    template_name = 'article_detail.html'


class ArticleListView(ListView):
    queryset = Article.objects.all()
    template_name = 'article_list.html'


class TestErrorView(View):
    def get(self, *args, **kwargs):
        raise Exception
