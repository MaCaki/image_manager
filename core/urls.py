from django.conf.urls import url

from . import views
from . import api

app_name = 'core'

urlpatterns = [
    url(r'^users/home', views.UserHomeView.as_view(), name='user-home'),
    url(
        r'^users/edit',
        views.AccountUpdateView.as_view(),
        name='account-update'
    ),
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
        r'^(?P<pk>[0-9]+)/grade$',
        views.GradeStudyView.as_view(),
        name='grade-study'
    ),
    url(
        r'^(?P<pk>[0-9]+)/create-patient$',
        views.PatientCreateView.as_view(),
        name='create-patient'
    ),
    url(
        r'^patient/(?P<pk>[0-9]+)/$',
        views.PatientDetailView.as_view(),
        name='patient-detail'
    ),
    url(
        r'^patient/(?P<patient_pk>[0-9]+)/eyelids/(?P<pk>[0-9]+)$',
        views.EyelidDetailView.as_view(),
        name='eyelid-detail'
    ),
    url(
        r'^patient/(?P<pk>[0-9]+)/upload_eyelids$',
        views.EyeLidUploadView.as_view(),
        name='upload-eyelids'
    ),
    #  Api endpoints.
    url(r'^api/v0/eyelids/$', api.EyeLidKeyGradeList.as_view())
]
