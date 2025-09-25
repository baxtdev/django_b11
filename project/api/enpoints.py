from django.urls import path,include

from rest_framework.routers import DefaultRouter

from .api import NewsViewSet,CategoryViewSet,UserRegisterViewSet,AcccountProfileViewSet
from .yasg import urlpatterns as url_doc

router = DefaultRouter()

router.register('news',NewsViewSet)
router.register('categories',CategoryViewSet)
router.register('accounts/register',UserRegisterViewSet)


urlpatterns = [
    # path('news/', NewsListAPIView.as_view(), name='news-list'),
    # path('news/<int:pk>/', NewsDetailAPIView.as_view(), name='news-delete'),
    # path('categories/', CategoryAPIVIew.as_view(), name='category-list'),
    path('',include(router.urls)),
    path('accounts/profile/',AcccountProfileViewSet.as_view(),name="acounts-profile-get")
]
urlpatterns+=url_doc