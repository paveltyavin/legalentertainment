from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^article/$', views.ArticleListView.as_view(), name='article_list'),
    url(r'^article/(?P<pk>\d+)$', views.ArticleDetailView.as_view(), name='article_detail'),
    url(r'^test/error/$', views.TestErrorView.as_view(), name='test_error'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    url(r'^$', views.HomeView.as_view(), name='home'),
)

if settings.DEBUG:
    from django.views.static import serve

    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
