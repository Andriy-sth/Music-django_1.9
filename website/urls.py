from django.conf.urls import url, include
from django.contrib import admin

from music import views

urlpatterns = [
    #home
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('music.urls'))
]
