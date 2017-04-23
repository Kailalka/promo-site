
from django.conf.urls import url, include
from django.contrib import admin
from blog import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^albums/$', views.albums, name='albums'),
	url(r'^contacts/$', views.contacts, name='contacts'),
	url(r'^posts/$', views.post_list, name='list'),
	url(r'^posts/(?P<post_id>\d+)/$', views.post_detail, name='detail'),
]
