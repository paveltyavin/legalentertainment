from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomeView.as_view()),
    url(r'^article/$', views.ArticleListView.as_view(), name='article_list'),
    url(r'^article/(?P<pk>\d+)$', views.ArticleDetailView.as_view(), name='article_detail'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    ]
