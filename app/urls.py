from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.home_view),
    url(r'^test/$',views.test),
    url(r'^about/$',views.about),
]
