from distutils.core import setup

setup(name='django-news',
      version='0.7',
      description='A django application for keeping your fans up to date...',
      author='Brandon R. Stoner',
      author_email='monokrome@monokro.me',
      url='http://monokro.me/',
      download_url='http://github.com/monokrome/django-news/',
      packages=['django.contrib.news'],
#      data_files=[
#             (
#                 'django/contrib/news/templates/news/',
#                 [
#                     'django/contrib/news/templates/news/base.html',
#                     'django/contrib/news/templates/news/article_list.html',
#                     'django/contrib/news/templates/news/article_detail.html',
#                 ]
#             ),
#      ],
)

