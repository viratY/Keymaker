from django.urls import path, re_path
import webApp.views as views

urlpatterns = [
    re_path(r'^customers/$',
        views.CustomerList.as_view(),
        name=views.CustomerList.name),
    re_path(r'^customers/(?P<pk>[0-9]+)$',
        views.CustomerDetail.as_view(),
        name=views.CustomerDetail.name),
    re_path(r'^keymakers/$',
        views.KeyMakerList.as_view(),
        name=views.KeyMakerList.name),
    re_path(r'^keymakers/(?P<pk>[0-9]+)$',
        views.KeyMakerDetail.as_view(),
        name=views.KeyMakerDetail.name),
    re_path(r'^requests/$',
        views.RequestList.as_view(),
        name=views.RequestList.name),
    re_path(r'^requests/(?P<pk>[0-9]+)$',
        views.RequestDetail.as_view(),
        name=views.RequestDetail.name),
    re_path(r'^charges/$',
        views.ChargeList.as_view(),
        name=views.ChargeList.name),
    re_path(r'^charges/(?P<pk>[0-9]+)$',
        views.ChargeDetail.as_view(),
        name=views.ChargeDetail.name),
    re_path(r'^$',
        views.ApiRoot.as_view(),
        name=views.ApiRoot.name),
]






