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
    url(r'^article/edit/$', 'django.contrib.news.views.edit_article', name='news_article_edit'),
    url(r'^article/edit/(?P<article_id>[\d]+)/$', 'django.contrib.news.views.edit_article', name='news_article_edit'),
    url(r'^(?P<page>[\d]+)/$', 'django.contrib.news.views.index', name='news_index'),
    url(r'^article/(?P<identifier>[\d]+)/$','django.contrib.news.views.article', name='news_article'),
    url(r'^article/(?P<identifier>[^/]+)/$','django.contrib.news.views.article', {'slugified':True}, name='news_article'),

    url(r'^rss/v1/(?P<url>.+)$', 'django.contrib.syndication.views.feed', {'feed_dict': rss_v1_feeds}, name='news_feed_rss'),
    url(r'^rss/v2/(?P<url>.+)$', 'django.contrib.syndication.views.feed', {'feed_dict': rss_v2_feeds}, name='news_feed_rss2'),
    url(r'^atom/v1/(?P<url>.+)$', 'django.contrib.syndication.views.feed', {'feed_dict': atom_v1_feeds}, name='news_feed_atom'),
    url(r'^$', 'django.contrib.news.views.index', name='news_index'),
)

