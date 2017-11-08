from django.conf.urls import url

from . import views

app_name = 'core'

urlpatterns = [
    url(r'^$', views.StudyIndexView.as_view(), name='study-index'),
    url(
        r'^(?P<pk>[0-9]+)/$',
        views.StudyDetailView.as_view(),
        name='study-detail'
    ),
    url(
        r'^create-study/$',
        views.StudyCreateView.as_view(),
        name='create-study'
    ),
    url(
        r'^delete-study/(?P<pk>[0-9]+)/$',
        views.StudyDeleteView.as_view(),
        name='delete-study'
    ),
    url(
        r'^create-patient/$',
        views.PatientCreateView.as_view(),
        name='create-patient'
    ),
    url(
        r'^patient/(?P<pk>[0-9]+)/$',
        views.PatientDetailView.as_view(),
        name='patient-detail'
    ),
]
