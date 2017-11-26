from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^news/(?P<News_id>[0-9]+)$', views.newsDetail, name='newsDetail'),
    url(r'^treatments/$', views.treatmentView, name='treatmentView'),
    url(r'^employees/$', views.employeeView, name='employeeView'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


