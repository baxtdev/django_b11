from django.urls import path,include

from rest_framework.routers import DefaultRouter

from .api import NewsListAPIView,NewsDetailAPIView,CategoryAPIVIew

router = DefaultRouter()

# router.register('news',NewsModelViewset)


urlpatterns = [
    path('news/', NewsListAPIView.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsDetailAPIView.as_view(), name='news-delete'),
    path('categories/', CategoryAPIVIew.as_view(), name='category-list'),
    path('',include(router.urls))
]