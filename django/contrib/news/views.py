from django.views.generic.list_detail import object_list,object_detail
from models import Article

RESULTS_PER_LIST_PAGE=3

def index(request, page=1):
    qs = Article.objects.filter(published=True).order_by('-created_on')

    return object_list(request, queryset=qs, template_object_name='article',\
        paginate_by=RESULTS_PER_LIST_PAGE, page=page)

def article(request, identifier, slugified=False):
    data = {
        'queryset': Article.objects.filter(published=True)
    }

    if slugified == False:
        data['object_id'] = identifier
    else:
        data['slug'] = identifier

    return object_detail(request, template_object_name='article', **data)

