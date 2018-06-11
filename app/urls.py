from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.home_view),
    url(r'^test/$',views.test),
    url(r'^about/$',views.about),
    url(r'^list_all/$', views.list_all),
    url(r'^add/(?P<comment>\w{1,50})/$', views.add)
]
