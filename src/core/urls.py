from django.conf.urls import url

from . import views
from core.views import HomePageView, MapPageView
from core.views import GoogleVerefication, EventsTodayPageView, EventsSoonPageView, EventDetailView, get_map, get_event_map, get_event_map_by_date
from django.http import HttpResponse
urlpatterns = [
	url(r'^googledf88e6599dbb7495\.html$', lambda r: HttpResponse("google-site-verification: googledf88e6599dbb7495.html", content_type="text/plain")),
	
	url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: ", content_type="text/plain")),
	#url(r'^googledf88e6599dbb7495\.html$', GoogleVerefication.as_view(), name='google_verification'),
	url(r'^events_todat/$', EventsTodayPageView.as_view(), name='events_today'),
	url(r'^events_soon/$', EventsSoonPageView.as_view(), name='events_soon'),
	#url(r'^map/$', MapPageView.as_view(), name='map'),
	url(r'^$', MapPageView.as_view(), name='map'),
	url(r'^contact/$', views.contact_admin, name='contact'),
	url(r'^submit/$', views.events_add, name='submit_event'),
	#url(r'^map/get_map/', get_map, name='get_map'),
	url(r'^get_map/', get_map, name='get_map'),
	url(r'^get_event_map/', get_event_map, name='get_event_map'),
	#get_event_map_by_date
	url(r'^get_event_map_by_date/', get_event_map_by_date, name='get_event_map_by_date'),
	url(r'^main/$', HomePageView.as_view(), name='home'),
	#url(r'^event_detail/(?P<pk>\d+)/$', EventDetailView.as_view(), name='event_detail'),
	url(r'^event_detail/(?P<slug>.+)/$', EventDetailView.as_view(), name='event_detail'),
	
]