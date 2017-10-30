from django.conf.urls import url

from . import views

app_name = 'core'

urlpatterns = [
    url(r'^$', views.StudyIndexView.as_view(), name='study_index'),
    url(
        r'^(?P<pk>[0-9]+)/$',
        views.StudyDetailView.as_view(),
        name='study_detail'
    )
]
