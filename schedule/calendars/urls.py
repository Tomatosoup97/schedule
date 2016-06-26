from django.conf.urls import url, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'meetings', views.MeetingViewSet)
router.register(r'suggestions', views.SuggestionViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'tags', views.TagViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]