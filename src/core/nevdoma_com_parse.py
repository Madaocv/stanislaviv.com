#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib
from urlparse import urljoin
from scrap_models import CoreEvent, database
import datetime
import sys  
from slugify import slugify
import os
import smtplib
reload(sys)  
sys.setdefaultencoding('utf-8')

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

    def save(self, item):
        query = CoreEvent.select().where(CoreEvent.source_href == item['href'])
        slug_query = CoreEvent.select(CoreEvent.slug)
        # for a in slug_query:
        #     print a.slug
        if query.exists():
            self.count_exists=self.count_exists+1
            print "query alredy exists %d %s" % (self.count_exists , item['title'])

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
                    status = 'draft',
                    source= 'nevdoma.com',
                    contact_number = '',
                    ticket = '',
                    category_id = 12,
                    latitude='',
                    longitude='',
                    photo=item['photo'],
                    location_false = item['location'],
                    vk_href = '',
                    fb_href = '',


                    
                )
            data.save()
            # try:
            #     data.save()
            #     self.count_good=self.count_good+1
            #     print "Good saving : %d"%self.count_good
            # except:
            #     self.count_error=self.count_error+1
            #     print "Erorr with saving : %d"%self.count_error
            #     self.trouble_url_list.append(item['href'])


    def parse_event_page(self, url):
        ###

        ###
        page = urllib.urlopen(url)
        soup = BeautifulSoup(page, "html.parser")
        item = {}
        #print "*****************EVENT***************************"
        current_url_page = page.geturl()
        #print "URL",current_url_page
        img = soup.find('img', attrs={'class': 'img-responsive img-rounded center-block'})['src']
        
        if 'http://' not in img:
            img_true = urljoin(current_url_page, img)
            #print "PICTURE ",img_true
            img_name = img_true.split('/')[-1]
            img_name =''.join(img_name)
            item['photo']= img_name
            path='../today_if_root/media/'
            fullfilename = os.path.join(path, img_name)
            urllib.urlretrieve(img_true, fullfilename)
        href = url
        #print 'href:',href
        item['href'] = href
        #print "-----title----------"
        title=soup.h3.string
        #print title
        item['title'] =title
        title_split_for_slug = href.split('/')[-1]
        slug =''.join(title_split_for_slug)
#item['slug']=slugify(item['title'], to_lower=True)
        item['slug']=slug
        #print "SLUG",slug
        table = soup.findAll('div', attrs={'class': 'col-sm-8 col-md-9'})
        for x in table:
            #print "-----datetime----------"
            first = x.find('p')
            first_span = first.find('span')
            if first_span.find_previous_sibling()['class'] == [u'fa', u'fa-calendar']:
                #print 'Час і дата повністю:', first_span.text

                datetime_ = first_span.text
                date = datetime.datetime.strptime(datetime_, '%d-%m-%Y %H:%M').strftime('%Y-%m-%d')
                
                time = datetime.datetime.strptime(datetime_, '%d-%m-%Y %H:%M').strftime('%H:%M')
                #print "DATATYPE", time
                item['date'] = date
                item['time'] = time
                #print "DATATYPE", type(time)
            #print "-----location----------"
            next_p = first.find_next_sibling()
            next_span = next_p.find('span')
            if next_span.find_previous_sibling()['class'] == [u'fa', u'fa-map-marker']:
                #print 'Місце проведення:',next_span.text
                item['location'] =next_span.text
            #print "-------descript_div--------"
            descript_div = next_p.find_next_sibling()
            #print "Опис події :",descript_div.text
            item['description'] =descript_div.text
            #print "-------price--------"
            price_div = descript_div.find_next_sibling()
            price =  price_div.text.strip()
            if price.split(' ')[0] == 'Ціна:'.decode('utf-8'):
                price2 = price.split(' ')[1:]
                true_price = ' '.join(price2)
                #print "Ціна події :",true_price
                item['price'] =true_price
        #print "ITEM",item
        self.save(item)

    def run_parser(self):
        try:
            site = urllib.urlopen('http://nevdoma.com/events')
            soup = BeautifulSoup(site, "html.parser")
            div_ = soup.findAll('div','col-sm-8 col-md-9 col-xs-7')
            for a in div_ :
                if a.find('a')['href']:
                    if 'http://' not in a.find('a')['href']:
                        l2 = urljoin(site.geturl(), a.find('a')['href'])
                        self.parse_event_page(l2)


            trouble_url_list_to_send='\r\n'.join(self.trouble_url_list)
            main_text="\r\n".join([
              "Нові добавдення :%d"%self.count_good,
              "Кількість подій які хуй там ше раз відскапиш, вони вже ска є в нашій базі :%d"%self.count_exists,
              "Проблемні урли :%d"%self.count_error,
              trouble_url_list_to_send,
              ])
            msg = "\r\n".join([
              "From: Від старічка крона",
              "To: Нормальному пацанчику месага@",
              "Subject: Результати скрапінгу Nevdoma.com",
              "",
              main_text,
              ])


            try:  
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                server.login(gmail_user, gmail_password)
                server.sendmail(sent_from, to, msg)
                server.close()

                print 'Email sent!'
            except:  
                print 'Something went wrong...'
        except:        
            msg = "\r\n".join([
                  "From: Пездарики крону",
                  "To: Нормальному пацанчику месага@",
                  "Subject: Результати скрапінгу Nevdoma.com",
                  "",
                  "Пизда прийшла сушіть весла",
                  ])


            try:  
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                server.login(gmail_user, gmail_password)
                server.sendmail(sent_from, to, msg)
                server.close()

                print 'Email sent!'
            except:  
                print 'Something went wrong...'


        

database.connect()
a=ParserNevdomaCom()
a.run_parser()
#a.parse_event_page('http://nevdoma.com/events/smm_gym_2_0_2017-05-30_19_00')
