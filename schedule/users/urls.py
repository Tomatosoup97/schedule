from django.conf.urls import url, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'hosts', views.HostProfileViewSet)
router.register(r'clients', views.ClientProfileViewSet)

urlpatterns = [
    url(r'^users/me/$',
        views.UserCurrentView.as_view(),
        name='users-current'),
    url(r'^', include(router.urls)),
    url(r'^', include(router.urls)),
]