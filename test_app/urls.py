from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import HomeView, TestFormView, SmilesView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'new-user', SmilesView.as_view(), name='register'),
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^test-form/$', TestFormView.as_view(), name="test-form"),
)
