from django.db import models
from django.utils.text import slugify
from django.contrib.sites.models import Site
from mithril.models import Whitelist


class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date']
        verbose_name_plural = "news"
        db_table = 'news'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/news/%s/' % self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(News, self).save(*args, **kwargs)


class SiteACL(models.Model):
    site = models.OneToOneField(Site)
    whitelist = models.ForeignKey(Whitelist, related_name='site_acl')

    class Meta:
        db_table = 'site_acl'
