from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns=[
     url(r'^$', views.index, name='welcome'),
     url(r'^accounts/profile/update', views.update_profile, name='profile'),
     url(r'^accounts/profile', views.my_profile, name='myaccount'),
     url(r'^user/(?P<user_id>\d+)$', views.user_profile, name='aboutuser'),
     url(r'^upload/', views.upload_project, name='upload_project'),
     url(r'^api/profiles/$', views.ProfileList.as_view()),
     url(r'^api/projects/$', views.ProjectList.as_view()),
     url(r'^search/', views.search_results, name='search_results'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)