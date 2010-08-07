### This is a non-standard method of checking the availability of different modules in django.
### TODO: Find/create a more centralized, simple, standard method of doing this.
from exceptions import ImportError
from django.conf import settings

###
# Check if comments are available
if hasattr(settings, 'INSTALLED_APPS') and 'django.contrib.comments' in settings.INSTALLED_APPS:
    comments = True
else:
    comments = False

###
# Check if markup is available
if hasattr(settings, 'INSTALLED_APPS') and 'django.contrib.markup' in settings.INSTALLED_APPS:
    markup = True
    markup_filters = []

    # Check for support methods
    try:
        import textile
        markup_filters.append('textile')
    except ImportError:
        pass

    try:
        import markdown
        markup_filters.append('markdown')
    except ImportError:
        pass

    try:
        import docutils
        markup_filters.append('restructuredtext')
    except ImportError:
        pass
else:
    markup = False
    markup_filters = []

