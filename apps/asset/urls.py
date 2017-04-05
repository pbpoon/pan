from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/', views.FileUploadView.as_view(), name='addfile'),
    # url(r'^people/(?P<pk>\d+)/$', views.PeopleView.as_view(), name='people'),
    # url(r'^(?P<name>\w+)/$', views.AccountDetailView.as_view(), name='detail'),
    # url(r'^$', views.AccountListView.as_view(), name='index'),

]
