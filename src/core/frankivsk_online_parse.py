#-*- coding: utf-8 -*-
import dateparser
from bs4 import BeautifulSoup
import urllib
#import urllib2
#from urlparse import urljoin
from scrap_models import CoreEvent, database
import datetime
import sys  
from slugify import slugify
import os
import smtplib
import requests
import requests
import shutil
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from difflib import SequenceMatcher
x=7
start_day_for_parse = datetime.datetime.now()
end_day_for_parse=datetime.datetime.now()+datetime.timedelta(days=x)
gener = [start_day_for_parse + datetime.timedelta(days=x) for x in range(0, (end_day_for_parse-start_day_for_parse).days)]
url_list_for_parse =[]
for date in gener:
    url_list_for_parse.append("http://frankivsk-online.com/calendar/?date=%s"%date.strftime('%Y-%m-%d'))

######
gmail_user ='ucantdream@gmail.com'
gmail_password = 'Hello123Melyacv'
sent_from = gmail_user  
to = [gmail_user]

class ParserNevdomaCom(object):
    count_good = 0
    count_exists = 0
    count_error = 0
    trouble_url_list=[]

    def __init__(self):
        pass
    def similar(self, a, b):
        return SequenceMatcher(None, a, b).ratio()

    def find_location(self, some_text):
        result = {}
        if 'Urban Space 100' in some_text or 'вул. Михайла Грушевського, 19' in some_text:
            result['status'] = 'published'
            result['latitude'] = 48.92175899999999
            result['longitude'] = 24.71393290000003
            result['id'] =1
        elif 'Yoga IF School' in some_text or 'вул. Стуса, 35а' in some_text:
            result['status'] = 'published'
            result['latitude'] = 48.93361540000001
            result['longitude'] = 24.74979129999997
            result['id'] =2
        elif 'Grand America' in some_text or 'вул. Чорновола, 23' in some_text:
            result['status'] = 'published'
            result['latitude'] = 48.917457
            result['longitude'] = 24.706650999999965
            result['id'] =3
        elif 'Pasage Gartenberg' in some_text or 'вул. Незалежності, 3' in some_text:
            result['status'] = 'published'
            result['latitude'] = 48.920967
            result['longitude'] = 24.708329999999933
            result['id'] =4
        elif 'Промприлад' in some_text or 'вул. Сахарова, 23' in some_text:
            result['status'] = 'published'
            result['latitude'] = 48.913957
            result['longitude'] = 24.71278499999994
            result['id'] =5
        elif 'Виставковий зал Національної спілки художників України' in some_text or 'вул. Незалежності, 53' in some_text:
            result['status'] = 'published'
            result['latitude'] = 48.9191146
            result['longitude'] = 24.715609599999993 
            result['id'] =6
        elif 'вул. Шевченка, 3' in some_text:
            result['status'] = 'published'
            result['latitude'] = 48.919179
            result['longitude'] = 24.706259000000045  
            result['id'] =7
        elif 'Івано-Франківський Центр сучасного мистецтва' in some_text or 'вул. Шевченка, 1' in some_text:
            result['status'] = 'published'
            result['latitude'] = 48.91963380000001
            result['longitude'] = 24.706307100000004
            result['id'] =8
        elif 'Бастіон' in some_text or 'провулок Фортечний, 1' in some_text:
            result['status'] = 'published'
            result['latitude'] = 48.9221647
            result['longitude'] = 24.707898200000045 
            result['id'] =9    
        elif 'Міжнародний аеропорт «Івано-Франківськ»' in some_text or 'вулиця Євгена Коновальця, 264 А' in some_text:
            result['status'] = 'published'
            result['latitude'] = 48.887584
            result['longitude'] = 24.70699669999999 
            result['id'] =10
        elif 'Івано-Франківський краєзнавчий музей' in some_text or 'вул. Галицька, 4а' in some_text:
            result['status'] = 'published'
            result['latitude'] = 48.922723
            result['longitude'] = 24.710380999999984 
            result['id'] =11   
        elif 'вул. Т.Шевченка, 3' in some_text:
            result['status'] = 'published'
            result['latitude'] = 48.919179
            result['longitude'] = 24.706259000000045
            result['id'] =12
        else:
            result['status'] = 'draft'
            result['latitude'] = ''
            result['longitude'] = ''
            result['id'] =13
        return result

    def find_category_id(self, some_text):
        if 'Семінари/Лекції' in some_text:
            return 4
        elif 'Мистецтво' in some_text:
            return 11
        elif 'Нічне життя' in some_text:
            return 1
        elif 'Музика' in some_text:
            return 2
        elif 'Спорт' in some_text:
            return 3
        elif 'Театр' in some_text:
            return 9
        elif 'Екскурсії' in some_text:
            return 7
        elif 'Фестивалі' in some_text:
            return 8
        # elif 'Семінари/Лекції' in some_text:
        #     return 4
        elif 'Література' in some_text:
            return 6
        elif 'Тренінги/Майстер-класи' in some_text:
            return 5
        elif 'Бізнес' in some_text:
            return 10
        else:
            return 12
    def save(self, item):
        query = CoreEvent.select().where(CoreEvent.slug == item['slug'], CoreEvent.event_day == item['date'], CoreEvent.event_time == item['time'])
        slug_query = CoreEvent.select(CoreEvent.slug)
        for a in CoreEvent.select():
            print('Persent % :',self.similar(a.title, item['title']),a.title,'+',item['title'])
        if query.exists():
            self.count_exists=self.count_exists+1
            print("query alredy exists %d %s" % (self.count_exists , item['title']))

            #return True
        else:
            data = CoreEvent(
                    title = item['title'],
                    source_href = item['href'],
                    event_day = item['date'],
                    event_time = item['time'],
                    location = item['location'],
                    description = item['description'],
                    price = item['price'],
                    slug =item['slug'],
                    publish = datetime.date.today(),
                    status = item['status'],
                    source= 'frankivsk-online.com',
                    contact_number = '',
                    ticket = '',
                    category_id = item['category_id'],
                    latitude= item['latitude'],
                    longitude = item['longitude'],
                    photo=item['photo'],
                    location_false = item['location'],
                    vk_href = '',
                    fb_href = '',


                    
                )
            #data.save()
            try:
                data.save()
                self.count_good=self.count_good+1
                print( "Good saving : %d"%self.count_good)
            except:
                self.count_error=self.count_error+1
                print( "Erorr with saving : %d"%self.count_error)
                print( "Problem url:",item['href'])
                self.trouble_url_list.append(item['href'])
    def parse_event_page(self, url):
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})
        soup = BeautifulSoup(response.content, "html5lib") 
        item = {}
        item['href'] = url
        print (url)
        # пресет для функції find_category_id
        posible_category = soup.find_all('a',attrs={'rel': 'category tag'})
        posible_category_list = [a.text for a in posible_category]
        #print('Семінари/Лекції', posible_category_list)
        ##print('Gategory ID', self.find_category_id(posible_category_list))
        item['category_id'] = self.find_category_id(posible_category_list)
        #Кінець пошуку категорій
        try:
            title=soup.find('h1',attrs={'class': 'single--event--title'})
            title = title.text.strip()
        except:
            title=soup.find('h1',attrs={'class': 'places--title'})
            title = title.text.strip()
        item['title'] = title

        try:
            location = soup.find('p',attrs={'class': 'single--event--place__location'})
            location = location.text.strip()
            print('-------',location)
            print('Urban Space 100' in location or 'вул. Михайла Грушевського, 19' in location)
            print(self.find_location(location)['id'],'Місце проведення try:',location)
            print(self.find_location(location)['status'],self.find_location(location)['latitude'],self.find_location(location)['longitude'])
            item['status'] = self.find_location(location)['status']
            item['latitude'] = self.find_location(location)['latitude']
            item['longitude'] = self.find_location(location)['longitude']
        except:
            location = soup.find('span',attrs={'itemprop': 'addressLocality'})
            location = location.text.strip()
            #print('Місце проведення except:',location)
            item['status'] = self.find_location(location)['status']
            item['latitude'] = self.find_location(location)['latitude']
            item['longitude'] = self.find_location(location)['longitude']
        item['location'] =location
        try:
            price = soup.find('p',attrs={'class': 'single--event--tickets__price'})
            item['price'] =price.text
        except:
            item['price'] = 'Ціна не вказана'

        try:
            description = soup.find('div',attrs={'class': 'single--event--text'})
            description =description.text
            try:
                item['description'] =description.split('\n\nМітки')[0]
            except:
                item['description'] =description.text

        except:
            description = soup.find('main',attrs={'class': 'single--place--text'})
            description =description.text
            try:
                item['description'] =description.split('\n\nМітки')[0]
            except:
                item['description'] =description.text

        try:
            image = soup.find('img',attrs={'class': 'single--event--poster'})['src']
        except:
            image = soup.find('img',attrs={'itemprop': 'image'})['src']

        img_name = image.split('/')[-1]
        img_name =''.join(img_name)
        item['photo']= img_name
        path='../today_if_root/media/'
        #path = '/home/oeliiashiv/today_if_ua/src/today_if_root/media/'
        fullfilename = os.path.join(path, img_name)
        r = requests.get(image, stream=True, headers={'User-agent': 'Mozilla/5.0'})
        if r.status_code == 200:
            with open(fullfilename, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
        time = soup.find('p',attrs={'class': 'single--event--time'}) 
        #Цей трай якшо в події немає вопше часу на сайті
        try: 
            line=time.text.strip()
            #print 'line',line
            #print 'line2',line.splitlines()
            line2=' '.join(line.splitlines())
            #if ',' in time.text.strip():
            Listcount=[a.count(',') for a in line2.split('            ')]
            if time.text.strip().count(',') < 2 and '-' not in time.text.strip():
                print( "Single event")
                full_time =dateparser.parse(time.text.strip())
                print( 'full_time',full_time)
                date = full_time.strftime('%Y-%m-%d')
                time = full_time.strftime('%H:%M')
                item['date'] = datetime.datetime.strptime(date, '%Y-%m-%d').date()
                item['time'] = datetime.datetime.strptime(time, '%H:%M').time()
                time_to_slug =full_time.strftime('%H-%M')
                #print 'date',date,time
                first_part_slug = item['href'].split('/')[-2]
                slug = first_part_slug +'-' +date+'-' +time_to_slug
                item['slug']= slug
                #print item
                self.save(item)
            elif '-' in time.text.strip():
                print( "several")
                print( item['href'])
                time_range = time.text.strip().split('-')
                
                time_range_start =''.join(time_range[0])
                time_range_end =''.join(time_range[1])
                print( time_range_start,time_range_end)
                print( "-------Loop------")
                time_range_start=dateparser.parse(time_range_start)
                time_range_end=dateparser.parse(time_range_end)
                start_day_for_parse = datetime.datetime.now()
                end_day_for_parse= time_range_end
                step = datetime.timedelta(days=1)
                while start_day_for_parse <= end_day_for_parse + datetime.timedelta(days=1):
                    #print start_day_for_parse.date()
                    item['date'] = start_day_for_parse.date()
                    item['time'] = '19:00'
                    first_part_slug = item['href'].split('/')[-2]
                    slug = first_part_slug +'-' +str(start_day_for_parse.date())+'-'+'19_00'
                    item['slug']= slug
                    self.save(item)
                    start_day_for_parse += step
                print('Подія без часу яка повторюється декілька раз - ')
            
            elif len([i for i in Listcount if i>1]) == 0:
                #print line2.split('            ')
                #Listcount=[a.count(',') for a in line2.split('            ')]
                #print len([i for i in Listcount if i>1])
                list_with_several_singe_event = [dateparser.parse(''.join(d)) for d in line2.split('            ')]
                for a in list_with_several_singe_event:
                    date = a.strftime('%Y-%m-%d')
                    time = a.strftime('%H:%M')
                    time_to_slug =a.strftime('%H-%M')
                    item['date'] = datetime.datetime.strptime(date, '%Y-%m-%d').date()
                    item['time'] = datetime.datetime.strptime(time, '%H:%M').time()
                    first_part_slug = item['href'].split('/')[-2]+'-'+str(date)+'-'+str(time_to_slug)
                    #print 'slug ?',first_part_slug
                    item['slug']= first_part_slug
                    self.save(item)
            else:
                print( line2.split('            '))
                new_list_date=[]
                for a in line2.split('            '):
                    if a.count(':')==1:
                        #print a
                        new_list_date.append(a)
                    elif a.count(':')>1:
                        f= a.split(',')[0]
                        for a in a.split(',')[1:]:
                            #print f+','+a
                            new_list_date.append(f+','+a)
                list_with_several_singe_event= [dateparser.parse(''.join(a)) for a in new_list_date]
                for a in list_with_several_singe_event:
                    date = a.strftime('%Y-%m-%d')
                    time = a.strftime('%H:%M')
                    time_to_slug =a.strftime('%H-%M')
                    item['date'] = datetime.datetime.strptime(date, '%Y-%m-%d').date()
                    item['time'] = datetime.datetime.strptime(time, '%H:%M').time()
                    first_part_slug = item['href'].split('/')[-2]+'-'+str(date)+'-'+str(time_to_slug)
                    #print 'slug ?',first_part_slug
                    item['slug']= first_part_slug
                    self.save(item)
        except:
            #Вот тут вот требуде поправити бо я сам хз чи норм зберігатиму
            item['slug']=url.split('/')[-2] +'-'+ str(datetime.date.today())
            #print '3234',item['slug']
            item['date'] =datetime.date.today()
            #print type(item['date'])
            tim = '19:00'
            tim2 = datetime.datetime.strptime(tim, "%H:%M").time()
            item['time'] = tim2
            print('Подія без часу', item)
            self.save(item)

            
    def run_parser(self, url):
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})
        soup = BeautifulSoup(response.content, "html5lib")
        span_ = soup.findAll('span','category-name')
        article_= soup.findAll('article',attrs={'class': 'events'})
        for x in article_:
            second = x.find('span')
            if second != None:
                if second.text.strip() != 'Кіно':
                    first = second.find_previous_sibling()
                    self.parse_event_page(first['href'])
    def generate_list_url_for_parse(self):
        #try:
        x=7
        start_day_for_parse = datetime.datetime.now()
        end_day_for_parse=datetime.datetime.now()+datetime.timedelta(days=x)
        gener = [start_day_for_parse + datetime.timedelta(days=x) for x in range(0, (end_day_for_parse-start_day_for_parse).days)]
        url_list_for_parse =[]
        for date in gener:
            url_list_for_parse.append("http://frankivsk-online.com/calendar/?date=%s"%date.strftime('%Y-%m-%d'))
        #print "url_list_for_parse",url_list_for_parse
        for a in url_list_for_parse:
            self.run_parser(a)


        trouble_url_list_to_send='\r\n'.join(self.trouble_url_list)
        main_text="\r\n".join([
          "Нові добавдення :%s"%self.count_good,
          "Кількість подій які хуй там ше раз відскапиш, вони вже ска є в нашій базі :%s"%self.count_exists,
          "Проблемні урли :%s"%self.count_error,
          trouble_url_list_to_send,
          ])
        #main_text=MIMEMultipart(main_text)
        #main_text.encode("ascii", errors="ignore")

        msg = "\r\n".join([
          "From: Від бродяги крона ",
          "To: Нормальному пацанчику месага@",
          "Subject: Результати скрапінгу frankivsk-online.com",
          "",
          main_text,
          ])
        #print('MSG', msg, type(msg))
        msg = msg.encode("utf-8", errors="ignore")


        #try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, msg)
        server.close()

        print( 'Email sent!')
        #except:  
        #    print( 'Something went wrong...')



d=ParserNevdomaCom()
#d.parse_event_page('http://frankivsk-online.com/events/literature/prezentatsiya-zbirky-virshiv-andriya-nehrycha/')
#d.parse_event_page('http://frankivsk-online.com/events/night-life/vystup-dj-malyar/')
d.generate_list_url_for_parse()