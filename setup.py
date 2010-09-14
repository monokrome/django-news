from distutils.core import setup, find_packages

setup(name='django-news',
      version='0.7',
      description='A django application for keeping your fans up to date.',
      zip_safe=False,
      include_package_data=True,
      packages=find_packages(),
      author='Brandon R. Stoner',
      author_email='monokrome@monokro.me',
      url='http://github.com/monokrome/django-news/',
      classifiers = [
          "Development Status :: 4 - Beta",
          "Environment :: Web Environment",
          "Intended Audience :: Developers",
          "Operating System :: OS Independant",
          "Programming Language :: Python",
          "Framework :: Django",
          "Topic :: Internet :: WWW/HTTP / :: Dynamic Content",
          "Topic :: Internet :: WWW/HTTP / :: Site Management",
      ],
)

