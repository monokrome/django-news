from django.utils.feedgenerator import Atom1Feed, Rss201rev2Feed, \
    RssUserland091Feed
from django.contrib.syndication.feeds import Feed, FeedDoesNotExist,\
    ObjectDoesNotExist
from models import Article

class LatestArticles(Feed):
    title = ""
    author_link = ''
    copyright = ''
    author_name = ''
    author_email = ''
    description = ''
    ttl = '1'

    title_template = 'feeds/news/article_title.html'
    description_template = 'feeds/news/article_description.html'

    def item_author_name(self, obj):
        if obj.author:
            return obj.author.get_full_name()

        return None

    def item_author_email(self, obj):
        if obj.author:
            return obj.author.email

        return None

    def item_pubdate(self, obj):
        return obj.created_on

    def item_link(self, obj):
        return obj.get_absolute_url()

    def items(self):
        return Article.objects.filter(published=True).order_by('-created_on')[:15]

class RSSv1LatestArticles(LatestArticles):
    link = "/rss/v1/latest/"
    feed_type = RssUserland091Feed

class RSSv2LatestArticles(LatestArticles):
    link = "/rss/v2/latest/"
    feed_type = Rss201rev2Feed

class AtomLatestArticles(LatestArticles):
    link = "/atom/v1/latest/"
    subtitle = LatestArticles.description
    feed_type = Atom1Feed

