from django.views.generic.list_detail import object_list,object_detail
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

