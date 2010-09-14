from django.views.generic.list_detail import object_list,object_detail
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from forms import NewsArticleForm
from models import Article
import availability

def index(request, page=1, max_count=3):
    qs = Article.objects.filter(published=True).order_by('-created_on')

    return object_list(request, queryset=qs, template_object_name='article',\
        paginate_by=max_count, page=page, extra_context={
            'comments_available': availability.comments
        })

def article(request, identifier, slugified=False):
    data = {
        'queryset': Article.objects.filter(published=True)
    }

    if slugified == False:
        data['object_id'] = identifier
    else:
        data['slug'] = identifier

    data['template_object_name'] = 'article'
    data['extra_context'] = {
        'comments_available': availability.comments
    }

    return object_detail(request, **data)

@login_required
def edit_article(request, article_id=None, posted=False):
    if article_id is None:
        article = None
    else:
        article = get_object_or_404(Article, pk=article_id)

    if article is not None:
        if request.user.has_perm('news.change_article') is False:
            raise Http404('You are not allowed to edit other user''s news articles.')
    else:
        if request.user.has_perm('news.add_article') is False:
            raise Http404('You are not allowed to post news articles.')

    editing = False

    if request.method == 'POST':
        if article is not None:
            form = NewsArticleForm(request.POST, instance=article)
            editing = True
        else:
            form = NewsArticleForm(request.POST)

        if form.is_valid():
            form.instance.author = request.user
            form.save()

        return HttpResponseRedirect(reverse('news_index'))

    else:
        if article_id is None:
            form = NewsArticleForm()
        else:
            form = NewsArticleForm(instance=article)
            editing = True

    return render_to_response('news/article_edit.html', {'form': form, 'editing': editing, 'article': article}, \
        context_instance=RequestContext(request))

@login_required
def delete_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    if request.user.has_perm('news.delete_article') or \
       request.user.is_superuser or \
       request.user is article.author:
        article.delete()

    return HttpResponseRedirect(reverse('news_index'))

