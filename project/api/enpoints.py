from django.urls import path,include

from rest_framework.routers import DefaultRouter

from .api import NewsViewSet,CategoryViewSet

router = DefaultRouter()

router.register('news',NewsViewSet)
router.register('categories',CategoryViewSet)


urlpatterns = [
    # path('news/', NewsListAPIView.as_view(), name='news-list'),
    # path('news/<int:pk>/', NewsDetailAPIView.as_view(), name='news-delete'),
    # path('categories/', CategoryAPIVIew.as_view(), name='category-list'),
    path('',include(router.urls))
]