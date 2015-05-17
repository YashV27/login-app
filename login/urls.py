from django.conf.urls import patterns,url

from login import views

urlpatterns = patterns('',
    url(r'^$',views.index,name='index'),
    url(r'^/signup',views.signup,name='signup'),
    url(r'^(?P<Username>)/editprofile/$',views.edit_profile,name='edit_profile'),
    url(r'^(?P<Username>)/profile/$',views.profile,name='profile'),
    url(r'^(?P<Username>)/changepassword/$',views.change_password,name='change_password'),
)    

