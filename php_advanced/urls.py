"""php_advanced URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from example import views as example_views
from example import views_forms as example_views_forms

urlpatterns = [
    url(r'^hello$', example_views.hello_world),
    url(r'^hello/(?P<name>\w+)$', example_views.hello_name),
    url(r'^admin/', admin.site.urls),
    url(r'^gift_list_by_func_view/$', example_views.simple_list_view),


    url(r'^gift_list/$', example_views.GiftListView.as_view(), name='list_gfl'),
    url(r'^gift_list/add/$', example_views.PostCreateView.as_view(), name='add_gfl'),
    url(r'^gift_list/edit/(?P<pk>\d+)$', example_views_forms.PostEditView.as_view(), name='edit_gfl'),
    url(r'^gift_list/remove/(?P<pk>\d+)$', example_views.RemoveView.as_view(), name='remove_gfl'),

    url(r'^gift_list/(?P<giftlist_id>\d+)$', example_views.GiftView, name='gift_gfl'),
    url(r'^gift_list/edit/(?P<pk>\d+)$', example_views_forms.PostEditView.as_view(), name='edit_gift'),
    url(r'^gift_list/remove/(?P<pk>\d+)$', example_views.RemoveView.as_view(), name='remove_gift'),
]
