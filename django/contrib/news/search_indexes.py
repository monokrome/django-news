from haystack.indexes import *
from haystack import site
from models import Article

class ArticleIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    title = CharField(model_attr='title')
    body = CharField(model_attr='body')
    summary = CharField(model_attr='summary')
    slug = CharField(model_attr='slug')
    author = CharField(model_attr='author')
    categories = CharField(model_attr='category')

    def get_queryset(self):
        return Article.objects.all()

site.register(Article, ArticleIndex)

