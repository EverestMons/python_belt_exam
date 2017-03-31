from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', login, name='login'),
    url(r'^processlogin$', processlogin, name='processlogin'),
    url(r'^register$', register, name='register'),
    url(r'^processregister$', processregister, name='processregister'),
    url(r'^home$', home, name='home'),
    url(r'^logout$', logout, name='logout'),
    url(r'^additem$', additem, name='additem'),
    url(r'^processitem$', processitem, name='processitem'),
    url(r'^itempage/(?P<item_id>\d+)$', itempage, name='itempage'),
    url(r'^addtolist/(?P<item_id>\d+)$', addtolist, name='addtolist'),
    url(r'^removefromlist/(?P<item_id>\d+)$', removefromlist, name='removefromlist'),


]
