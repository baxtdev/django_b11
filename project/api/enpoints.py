from django.urls import path,include

from rest_framework.routers import DefaultRouter

from .api import NewsModelViewset

router = DefaultRouter()

router.register('news',NewsModelViewset)


urlpatterns = [
    path('',include(router.urls))
]