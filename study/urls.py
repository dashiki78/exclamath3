from django.conf.urls import url
from study import views


urlpatterns = [
   url(r'^$', views.first_page, name='first_page'),
   url(r'^dailynew/(?P<name>[ㄱ-힣]+)/(?P<date>\d{4}-\d{2}-\d{2})$', views.daily_new, name='daily_new'),
   url(r'^list/$', views.daily_list, name='daily_list'),
   url(r'^detail/(?P<id>\d+)$', views.daily_detail, name='daily_detail'),
   url(r'^update/(?P<id>\d+)/(?P<name>[ㄱ-힣]+)/(?P<date>\d{4}-\d{2}-\d{2})$', views.daily_update, name='daily_update'),
   url(r'^delete/(?P<id>\d+)$', views.daily_delete, name='daily_delete'),
   url(r'^course/(?P<level>[ㄱ-힣0-9\-]+)$', views.course_list, name='course_list'),
   # url(r'^course$', views.CourseViewSet, name='course_list'),
]
