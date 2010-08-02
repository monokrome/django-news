from django.conf.urls.defaults import *
from models import Article
from feeds import RSSv1LatestArticles, RSSv2LatestArticles, AtomLatestArticles

rss_v1_feeds = {
    'latest': RSSv1LatestArticles
}

rss_v2_feeds = {
    'latest': RSSv2LatestArticles,
}

atom_v1_feeds = {
    'latest': AtomLatestArticles,
}

urlpatterns = patterns('',
    url(r'^$', 'django.contrib.news.views.index', name='news_index'),
    url(r'^(?P<page>[\d]+)/$', 'django.contrib.news.views.index', name='news_index'),
    url(r'^article/(?P<identifier>[\d]+)/$','django.contrib.news.views.article', name='news_article'),
    url(r'^article/(?P<identifier>[^/]+)/$','django.contrib.news.views.article', {'slugified':True}, name='news_article'),

    url(r'^rss/v1/(?P<url>.+)$', 'django.contrib.syndication.views.feed', {'feed_dict': rss_v1_feeds}),
    url(r'^rss/v2/(?P<url>.+)$', 'django.contrib.syndication.views.feed', {'feed_dict': rss_v2_feeds}),
    url(r'^atom/v1/(?P<url>.+)$', 'django.contrib.syndication.views.feed', {'feed_dict': atom_v1_feeds}),
)

