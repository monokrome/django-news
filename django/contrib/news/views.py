from django.views.generic.list_detail import object_list,object_detail
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
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
    editing = False

    if request.method == 'POST':
        if article_id is not None:
            editing = True

        form = NewsArticleForm(request.POST)

        if form.is_valid():
            form.instance.author = request.user
            form.save()

        return HttpResponseRedirect(reverse('news_index'))

    else:
        if article_id is None:
            form = NewsArticleForm()
        else:
            article = get_object_or_404(Article, pk=article_id)
            form = NewsArticleForm(instance=article)
            editing = True

    return render_to_response('news/article_edit.html', {'form': form}, \
        context_instance=RequestContext(request))

