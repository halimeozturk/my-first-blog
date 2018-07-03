from django.conf.urls import url
from .views import *



urlpatterns = [

    url(r'^index/$',post_index,name='index'),
    url(r'^create/$',post_create,name='create'),
    url(r'^(?P<slug>\[\w-]+)/$',post_detail,name='detail'),
    url(r'^(?P<slug>\[\w-]+)/$',post_update,name='update'),
    url(r'^(?P<slug>\[\w-]+)/$',post_delete,name='delete'),

]
