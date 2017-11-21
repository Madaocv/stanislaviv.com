# -*- coding: utf-8 -*-
from django.shortcuts import render
from core.models import Event, Gategories, Partners
# Create your views here.
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
#from django.forms import ModelForm
#from django.db import models
#from django import 
from django import forms
from django.forms import ModelForm
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView, DeleteView, CreateView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
import datetime
from django.template.defaultfilters import slugify
from unidecode import unidecode
import timestring
import datetime
import dateparser
from django.utils import timezone
#+1date
#a=datetime.date.today() + datetime.timedelta(days=1)
from django.core import serializers
##### Send Email #####
from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings
#####
from PIL.ExifTags import TAGS
from PIL import Image
import magic
import imghdr

VALID_IMAGE_MIMETYPES = [
    "image"
]
#Add to a form containing a FileField and change the field names accordingly.
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

MAX_SIZE = 20971520
#MAX_SIZE = "5242880"

def valid_image_size(image, max_size=MAX_SIZE):
    #image.size = image.size
    #print('image.size',image.size)
    if image.size > max_size:
        return False
    return True

def clean_content(self):
    content = self.cleaned_data['content']
    content_type = content.content_type.split('/')[0]
    if content_type in settings.CONTENT_TYPES:
        if content._size > settings.MAX_UPLOAD_SIZE:
            raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(content._size)))
    else:
        raise forms.ValidationError(_('File type is not supported'))
    return content


def get_mimetype(fobject):
    mime = magic.Magic(mime=True)
    mimetype = mime.from_buffer(fobject.read(1024))
    fobject.seek(0)
    return mimetype

def valid_image_mimetype(fobject):
    # http://stackoverflow.com/q/20272579/396300
    mimetype = get_mimetype(fobject)
    if mimetype:
        return mimetype.startswith('image')
    else:
        return False
#>
#Event.objects.filter(event_day__gt=datetime.datetime.now(),status='published')
def get_event_map(request):
    if request.is_ajax():

        m = request.GET.get('object_event_id', None)
        true_event = Event.objects.get(id__exact=m)
        #print "Event_map",m
        z={}
        z['center']= [float(true_event.latitude), float(true_event.longitude)]
        z['icon']=true_event.category.icon
        response = {'first-text': 'Lorem Ipsum is simply dummy text', 'second-text': 'to make a type specimen book. It has '}
        return JsonResponse(z, safe=False)
def get_event_map_by_date(request):
    if request.is_ajax():
        m = request.GET.get('select_day', None)
        #print "MMMMM",dateparser.parse(m)
        f1 = dateparser.parse(m)
        f2 = datetime.datetime.strptime(str(f1), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
        events_in_day = Event.objects.filter(event_day__contains= f2, status='published')
        #events_in_day = Event.objects.filter(event_day__contains=datetime.datetime.now())
        #print "Yo yo yo",events_in_day

        response = {'first-text': 'Lorem Ipsum is simply dummy text', 'second-text': 'to make a type specimen book. It has '}
        #return JsonResponse(response)
        l=[]
        for a in events_in_day:
            z={}
            #print a.id, a.pk
            z['id']= "marker-%d" %a.id
            z['center']= [float(a.latitude), float(a.longitude)]
            #z['icon']="<i class='fa fa-star'></i>"
            z['icon']=a.category.icon
            z['title']=a.title
            z['price']=a.price
            z['image']=a.photo.url
            z['url']=a.get_absolute_url()
            #print "DDDDDDDDDDDDDDDDDDD",z['url']
            #z['center']= [a.latitude, a.longitude]
            #print z
            l.append(z)
        return JsonResponse(l, safe=False)

def get_map(request):
    #print 666666666666666666
    if request.is_ajax():
        #current_time = datetime.datetime.now().strftime('%H:%M')
        current_time_plus=datetime.datetime.now() + datetime.timedelta(hours=2)
        current_time_plus=current_time_plus.strftime('%H:%M')
        current_time_minus=datetime.datetime.now() - datetime.timedelta(hours=2)
        current_time_minus=current_time_minus.strftime('%H:%M')
        #print "ct+-",current_time_plus,current_time_minus,datetime.datetime.now()
        #event_today = Event.objects.filter(event_day__contains=datetime.date.today(),status='published',event_time__gte=current_time_plus)
        max_time_today_minus_two= datetime.datetime.combine(datetime.datetime.now(), datetime.time.max) - datetime.timedelta(hours=2)
        max_time_today = datetime.datetime.combine(datetime.datetime.now(), datetime.time.max)
        #print ">>>>>>>>>", Event.objects.filter(event_day__contains=datetime.date.today(),status='published',event_time__range=('21:00', '23:55'))

        if datetime.datetime.now().strftime('%H:%M') < '03:00':
            event_today = Event.objects.filter(event_day__contains=datetime.date.today(),status='published')
        elif datetime.datetime.now().strftime('%H:%M') < '22:00':
            #print "if"
            #event_today = Event.objects.filter(event_day__contains=datetime.date.today(),status='published')
            event_today = Event.objects.filter(event_day__contains=datetime.date.today(),status='published',event_time__gte=current_time_minus)
        else:
            #print "else"
            event_today = Event.objects.filter(event_day__contains=datetime.date.today(),status='published',event_time__range=('21:00', '23:55'))
        #print "Hello I an AJAX", event_today    
        response = {'first-text': 'Lorem Ipsum is simply dummy text', 'second-text': 'to make a type specimen book. It has '}
        
        l=[]
        for a in event_today:
            z={}
            #print a.id, a.pk
            z['id']= "marker-%d" %a.id
            z['center']= [float(a.latitude), float(a.longitude)]
            #z['icon']="<i class='fa fa-star'></i>"
            z['icon']=a.category.icon
            z['title']=a.title
            z['price']=a.price
            z['image']=a.photo.url
            z['url']=a.get_absolute_url()
            #print "DDDDDDDDDDDDDDDDDDD",z['url']
            #z['center']= [a.latitude, a.longitude]
            #print z
            l.append(z)
        return JsonResponse(l, safe=False)


class EventDetailView(DetailView):
    template_name = "today/event_detail.html"
    model = Event

    def get_context_data(self, **kwargs):
        print('kwargs----------',kwargs['object'],kwargs)
        a= kwargs['object']
        print(a,type(a),a.slug)
        total_views = r.incr('article:{}:views'.format(article.id))
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        #print context['object'].pk
        return context
        
class GoogleVerefication(TemplateView):
    template_name = "googledf88e6599dbb7495.html"
    def get_context_data(self, **kwargs):
        context = super(GoogleVerefication, self).get_context_data(**kwargs)

class HomePageView(TemplateView):

    template_name = "today/index.html"
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['partners'] = Partners.objects.all()
        #print "RRRR",context['partners']
        return context

class MapPageView(TemplateView):

    template_name = "today/map.html"
    def get_context_data(self, **kwargs):
        context = super(MapPageView, self).get_context_data(**kwargs)
        #,status='published'
        context['day'] = Event.objects.filter(event_day__contains=datetime.date.today(), status='published')
        context['plus_one_day'] = Event.objects.filter(event_day__contains=(datetime.date.today()+ datetime.timedelta(days=1)), status='published').order_by('event_time')
        context['plus_two_day'] = Event.objects.filter(event_day__contains=(datetime.date.today()+ datetime.timedelta(days=2)), status='published').order_by('event_time')
        context['plus_three_day'] = Event.objects.filter(event_day__contains=(datetime.date.today()+ datetime.timedelta(days=3)), status='published').order_by('event_time')
        context['plus_four_day'] = Event.objects.filter(event_day__contains=(datetime.date.today()+ datetime.timedelta(days=4)), status='published').order_by('event_time')
        context['plus_five_day'] = Event.objects.filter(event_day__contains=(datetime.date.today()+ datetime.timedelta(days=5)), status='published').order_by('event_time')
        context['plus_six_day'] = Event.objects.filter(event_day__contains=(datetime.date.today()+ datetime.timedelta(days=6)), status='published').order_by('event_time')
        context['plus_seven_day'] = Event.objects.filter(event_day__contains=(datetime.date.today()+ datetime.timedelta(days=7)), status='published').order_by('event_time')
        return context
# class ContactPageView(TemplateView):
#     template_name = "today/contact.html"
#     def get_context_data(self, **kwargs):
#         context = super(ContactPageView, self).get_context_data(**kwargs)

class EventsTodayPageView(ListView):
    model = Event
    template_name = "today/events.html"
    def get_context_data(self, **kwargs):
        context = super(EventsTodayPageView, self).get_context_data(**kwargs)
        #event_today = Event.objects.filter(event_day__contains=datetime.date.today(),status='published')
        current_time_minus=datetime.datetime.now() - datetime.timedelta(hours=2)
        current_time_minus=current_time_minus.strftime('%H:%M')
        if datetime.datetime.now().strftime('%H:%M') < '03:00':
            event_today = Event.objects.filter(event_day__contains=datetime.date.today(),status='published')
        elif datetime.datetime.now().strftime('%H:%M') < '22:00':
            #print "if"
            #event_today = Event.objects.filter(event_day__contains=datetime.date.today(),status='published')
            event_today = Event.objects.filter(event_day__contains=datetime.date.today(),status='published',event_time__gte=current_time_minus)
        else:
            #print "else"
            event_today = Event.objects.filter(event_day__contains=datetime.date.today(),status='published',event_time__range=('21:00', '23:55'))
        context['events'] = event_today
        #print context['events']
        categoryes_today=list(set([i.category for i in event_today]))
        context['categoryes']=categoryes_today
        return context

class EventsSoonPageView(ListView):
    model = Event
    template_name = "today/events.html"
    def get_context_data(self, **kwargs):
        context = super(EventsSoonPageView, self).get_context_data(**kwargs)
        event_soon = Event.objects.filter(event_day__gt=datetime.datetime.now(),status='published')
        context['events'] = event_soon
        categoryes_soon=list(set([i.category for i in event_soon]))
        context['categoryes']=categoryes_soon
        return context

def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret

def events_add(request):
    # was form posted?
    if request.method == "POST":
        photo_check = request.FILES.get('photoXXX')
        #print get_exif(photo_check)
        #print('photo_check',get_mimetype(photo_check))
        # was form add button clicked?
        #print valid_image_mimetype(photo_check)
        #print imghdr.what(photo_check)
        if request.POST.get('add_button') is not None:
            #print('MIMETYPE PHOTO',get_mimetype(photo_check))
            #print('Valid mimetype', valid_image_mimetype(photo_check))
            #print('valid_image_size',valid_image_size(photo_check))
            # errors collection
            errors = {}
            event_attr={}
            # validate user input
            title = request.POST.get('title', '').strip()
            if not title:
                errors['title'] = u"Назва події є обов'язковою"
            else:
                event_attr['title'] = title
            event_attr['slug']=Event.generate_slug(title)
            #опис
            description = request.POST.get('description', '').strip()
            # if not description:
            #     errors['description'] = u"Опишіть будь ласка шо там відбуватиметься"
            # else:
            event_attr['description'] = description
            #проведення
            event_day = request.POST.get('event_day', '').strip()
            if not event_day:
                errors['event_day'] = u"Дата проведення є обов'язковою"
            else:
                try:
                    datetime.datetime.strptime(event_day, '%d/%m/%Y')
                    #datetime.datetime.strptime(event_day, '%Y-%m-%d')
                except Exception:
                    errors['event_day'] = \
                        u"Введіть коректний формат дати (напр. 1984-12-30)"
                else:
                    e = datetime.datetime.strptime(event_day, '%d/%m/%Y').strftime('%Y-%m-%d')
                    event_attr['event_day'] = e
            #час проведення
            event_time = request.POST.get('event_time', '').strip()
            #print 777,event_time
            if not event_time:
                errors['event_time'] = u"Час проведення є обов'язковим, пишіть приблизно якшо не знаєте"
            else:
                try:
                    datetime.datetime.strptime(event_time, '%H:%M')
                    #print datetime.datetime.strptime(event_day, '%Y-%m-%d')
                except Exception:
                    errors['event_time'] = \
                        u"Введіть коректний формат часу (напр. 12:30)"
                else:
                    event_attr['event_time'] = event_time
                    #print 33333,data['event_time']
            #місце проведення
            location = request.POST.get('locationS', '').strip()
            #print 1,location
            if not location:
                errors['location'] = u"Напишіть локацію"
            else:
                event_attr['location'] = location
                event_attr['latitude'] = request.POST.get('lat', '').strip()
                event_attr['longitude'] = request.POST.get('lng', '').strip()

            event_group = request.POST.get('category', '').strip()
            if not event_group:
                errors['category'] = u"Оберіть категорію для події"
            else:
                groups = Gategories.objects.filter(pk=event_group)
                if len(groups) != 1:
                    errors['category'] = u"Оберіть коректну категорію"
                else:
                    event_attr['category'] = groups[0]
            photo = request.FILES.get('photoXXX')
            if not photo:
                errors['photo'] = u"Оберіть якусь фотографію"
            elif photo and not valid_image_mimetype(photo):
                errors['photo'] = u"Файл повинен бути зображенням"
            elif photo and not valid_image_size(photo):
                errors['photo'] = u"Розмір файлу повин бути меншим ніж 20МБ"
            else:
                event_attr['photo'] = photo
            #data={
            event_attr['contact_number'] = request.POST.get('contact_number')
            event_attr['price'] = request.POST.get('price')
            event_attr['ticket'] = request.POST.get('ticket')
            event_attr['source'] = 'user'
            event_attr['source_href'] = ''
            event_attr['status'] = 'draft'
             #'publish':timezone.now(),
            # }

            # save student
            if not errors:
                #print "event_attr",event_attr
                event = Event(**event_attr)
                event.save()
                event_name_t_letter = event_attr['title']
                event_name_to_letter = u''.join(event_name_t_letter).encode('utf-8')
                message1="\r\n".join([
                              "Якимось мадаонером добавлена наступна подія :%s"%event_name_to_letter,
                              "Прікінь, сам в ахує !!!",
                              "АУЄ фарту-масть",
                              ])
                send_mail(
                        'Нова подія від руки ', 
                        message1, 
                        'yakuys_madaoner_yebanuy@xuy.com', 
                        [settings.EMAIL_HOST_USER]
                        )
                # redirect to students list
                return HttpResponseRedirect(
                    u'%s?status_message=Подію успішно додано! Адміністрація перегляне і опублікує' %
                    reverse('core:events_today'))
            else:
                # render form with errors and previous user input
                return render(request, 'today/submit.html',
                    {'groups': Gategories.objects.all().order_by('id'),
                     'errors': errors})
        # elif request.POST.get('cancel_button') is not None:
        #     # redirect to home page on cancel button
        #     return HttpResponseRedirect(
        #         u'%s?status_message=Додавання студента скасовано!' %
        #         reverse('core:events_today'))
    else:
        # initial form render
        return render(request, 'today/submit.html',
            {'groups': Gategories.objects.all().order_by('id')})



class ContactForm_(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={"type":"text", "class":"form-control bordered"}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={"type":"text", "class":"form-control bordered"}))
    from_email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={ "class":"form-control bordered"}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={"class":"form-control bordered"}))

def contact_admin(request):
    # check if form was posted
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        #form = ContactForm(request.POST)
        #form = ContactForm(request.POST)
        form = ContactForm_(request.POST or None)
        #print "I want check you form text !"
        # check whether user data is valid:
        #print form.is_valid()
        if form.is_valid():
            # send email
            #print "FORM IS VALID"
            name1 = form.cleaned_data['name']
            name2 = u''.join(name1).encode('utf-8')
            subject1 = form.cleaned_data['subject']
            message1 = form.cleaned_data['message']
            message2 = u''.join(message1).encode('utf-8')
            from_email1 = form.cleaned_data['from_email']
            from_email2 = u''.join(from_email1).encode('utf-8')
            message_s="\r\n".join([
                              "Якийсь додік %s написав мессагу"%name2,
                              "Його емейл адрес : %s"%from_email2,
                              "Відповісти чи послати його нахуй ?",
                              ])
            #print "From email",from_email1

            try:
                send_mail(subject1, message_s, from_email1, [settings.EMAIL_HOST_USER])
            except Exception:
                message = u'Під час відправки листа виникла непередбачувана ' \
                    u'помилка. Спробуйте скористатись даною формою пізніше.'
            else:
                message = u'Повідомлення успішно надіслане!'

            # redirect to same contact page with success message
            return HttpResponseRedirect(
                u'%s?status_message=%s' % (reverse('core:contact'), message))
        else:
            print("BAD FORM")

    # if there was not POST render blank form
    else:
        form = ContactForm_()

    return render(request, 'today/contact.html', {'form': form})

