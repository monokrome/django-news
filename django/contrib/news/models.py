from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import datetime
import re

SUMMARY_MAX_LENGTH = 768

class Category(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True)
    name = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        if not self.parent:
            return self.name

        return '%s of %s' % self.name, self.parent.name

class Article(models.Model):
    """A single news entry."""
    title = models.CharField(max_length=64)
    body = models.TextField()
    summary = models.TextField(blank=True)
    slug = models.SlugField(blank=True, unique=True)
    published = models.BooleanField(default=False)
    created_on = models.DateTimeField()
    author = models.ForeignKey(User,null=True,blank=True)
    category = models.ManyToManyField(Category,related_name='articles',null=True,blank=True)

    @models.permalink
    def get_absolute_url(self):
        return ('news_article', [str(self.id)])

    def save(self, force_insert=False, force_update=False):
        if self.summary == None:
            if len(self.body) > SUMMARY_MAX_LENGTH:
                self.summary = self.body[0:(SUMMARY_MAX_LENGTH-1)]
            else:
                self.summary = self.body

        if not self.created_on:
            self.created_on = datetime.now()

        self.slug = slugify(self.title)

        super(Article,self).save(force_insert, force_update)

    def __unicode__(self):
        return self.title

