from django.conf.urls import url
import psw.views


urlpatterns = [
    url(r'^$', psw.views.index, name='index'),
    # url(r'^reg/', psw.views.reg, name='reg'),
    url(r'^add/', psw.views.add, name='add'),
    # url(r'^edit/(?P<chain_id>\d+)', psw.views.edit, name='edit'),
    url(r'^view/(?P<chain_id>\d+)', psw.views.view, name='view'),
]
