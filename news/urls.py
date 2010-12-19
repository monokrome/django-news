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
    url(r'^$', 'news.views.index', name='news_index'),
    url(r'^(?P<page>[\d]+)/$', 'news.views.index', name='news_index'),

    url(r'^article/edit/$', 'news.views.edit_article', name='news_article_edit'),
    url(r'^article/edit/(?P<article_id>[\d]+)/$', 'news.views.edit_article', name='news_article_edit'),
    url(r'^article/delete/(?P<article_id>[\d]+)/$', 'news.views.delete_article', name='news_article_delete'),
    url(r'^article/(?P<identifier>[\d]+)/$','news.views.article', name='news_article'),
    url(r'^article/(?P<identifier>[^/]+)/$','news.views.article', {'slugified':True}, name='news_article'),

    url(r'^rss/v1/(?P<url>.+)$', 'django.contrib.syndication.views.feed', {'feed_dict': rss_v1_feeds}, name='news_feed_rss'),
    url(r'^rss/v2/(?P<url>.+)$', 'django.contrib.syndication.views.feed', {'feed_dict': rss_v2_feeds}, name='news_feed_rss2'),
    url(r'^atom/v1/(?P<url>.+)$', 'django.contrib.syndication.views.feed', {'feed_dict': atom_v1_feeds}, name='news_feed_atom'),
)

