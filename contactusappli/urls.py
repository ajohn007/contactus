from django.urls import path,include

from .import views

from django.conf.urls import url


urlpatterns = [
    path('',views.index,name="index"),
    path('create',views.create_user,name='create'),
    url(r'^api/contactus$', views.contactDetails, name = 'contactDetails')
]