# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

def upload_location(instance, filename):
    return "%s/%s" %(event.id, filename)

class Event(models.Model):
    STATUS_CHOICES = (('published', 'Published'), ('draft', 'Draft'),)
    title = models.CharField(max_length=250, verbose_name=u"Назва події")
    #slug = models.SlugField(max_length=250, unique_for_date='publish',unique=True)
    slug = models.SlugField(max_length=250, unique_for_date='publish',blank=True,default='')
    category = models.ForeignKey('Gategories', verbose_name=u"Категорія", blank=False, null=True, on_delete=models.PROTECT)
    photo = models.ImageField(blank=True,verbose_name=u"Фото",null=True)
    description = models.TextField(blank=True,null=True, verbose_name=u"Опис події")
    publish = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    event_day = models.DateField(blank=False, verbose_name=u"Дата проведення події", null=True)
    event_time = models.TimeField(blank=False, verbose_name=u"Час проведення події", null=True)
    location_false = models.CharField(blank=True,null=True,max_length=550, verbose_name=u"Шаблонна Адреса/Місце проведення",default='')
    location = models.CharField(max_length=550, verbose_name=u"Адреса/Місце проведення",default='')
    latitude = models.CharField(blank=True, max_length=250, verbose_name=u"latitude",default='')
    longitude = models.CharField(blank=True, max_length=250, verbose_name=u"longitude",default='')
    contact_number = models.CharField(blank=True, max_length=250, verbose_name=u"Контактний телефон",default='')
    price = models.CharField(blank=True, max_length=250, verbose_name=u"Ціна",default='')
    ticket = models.CharField(blank=True, max_length=250, verbose_name=u"Квитки",default='')
    source = models.CharField(blank=True, max_length=250, verbose_name=u"Джерело",default='user')
    source_href = models.URLField(blank=True, max_length=250, verbose_name=u"Посилання на джерело",default='')
    vk_href = models.URLField(blank=True,null=True, max_length=250, verbose_name=u"Посилання vk", default='')
    fb_href = models.URLField(blank=True,null=True, max_length=250, verbose_name=u"Посилання fb", default='')
    
    class Meta:
        ordering = ('-publish',)
        verbose_name = u"Подія"
        verbose_name_plural = u"Події"

    def __str__ (self):
        return self.title

    @classmethod
    def generate_slug(self, title):
        count = 1
        slug = slugify(title)

        def _get_query(slug):
            if Event.objects.filter(slug=slug).count():
                return True

        while _get_query(slug):
            slug = slugify(u'{0}-{1}'.format(title, count))
            # make sure the slug is not too long
            while len(slug) > Event._meta.get_field('slug').max_length:
                title = title[:-1]
                slug = slugify(u'{0}-{1}'.format(title, count))
            count = count + 1
        return slug
#    def __unicode__(self):
#        return u"%s %s" % (self.first_name, self.last_name)    

#    def get_absolute_url(self):
#        return reverse('core:event_detail', args=[self.publish.year, self.publish.strftime('%m'), self.publish.strftime('%d'), self.slug])
    

    def get_absolute_url(self):
       #return reverse("core:event_detail", kwargs={"pk": self.pk})
       return reverse("core:event_detail", kwargs={"slug": self.slug})

#<a href = "{% url 'article' article.pk %}">
class Gategories(models.Model):
    """Group Model"""

    class Meta(object):
        verbose_name = u"Категорія"
        verbose_name_plural = u"Категорії"

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Назва")
    slug = models.SlugField(max_length=250,default='',unique=True)
    icon = models.CharField(blank=True, max_length=250, verbose_name=u"Іконка на карті",default='')
    def __str__ (self):
        return self.title

class Partners(models.Model):
    """Group Model"""

    class Meta(object):
        verbose_name = u"Партнер"
        verbose_name_plural = u"Партнери"
    title = models.CharField(max_length=250, verbose_name=u"Як називається партнер",blank=True,null=True,default='')
    photo = models.ImageField(blank=True,verbose_name=u"Фото партнера",null=True)
    source_href = models.URLField(blank=True, max_length=250, verbose_name=u"Посилання на партнера")
    def __str__ (self):
        return self.title