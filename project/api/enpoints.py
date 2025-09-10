from django.urls import path,include

from rest_framework.routers import DefaultRouter

from .api import NewsListAPIView,NewsDetailAPIView

router = DefaultRouter()

# router.register('news',NewsModelViewset)


urlpatterns = [
    path('news/', NewsListAPIView.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsDetailAPIView.as_view(), name='news-delete'),
    path('',include(router.urls))
]