### This is a non-standard method of checking the availability of different modules in django.
### TODO: Find/create a more centralized, simple, standard method of doing this.
from exceptions import ImportError
from django.conf import settings
from django.utils import datastructures

###
# Check if comments are available
if hasattr(settings, 'INSTALLED_APPS') and 'django.contrib.comments' in settings.INSTALLED_APPS:
    comments = True
else:
    comments = False

markup_filters = datastructures.SortedDict()

###
# Check if markup is available
if hasattr(settings, 'INSTALLED_APPS') and 'django.contrib.markup' in settings.INSTALLED_APPS:
    markup = True
else:
    markup = False

# Check for supported markup methods
try:
    import textile

    markup_filters['textile'] = True
except ImportError:
    markup_filters['textile'] = False

try:
    import markdown

    markup_filters['markdown'] = True
except ImportError:
    markup_filters['markdown'] = False

try:
    import docutils

    markup_filters['restructuredtext'] = True
except ImportError:
    markup_filters['restructuredtext'] = False

