from django.urls import path

from .views import news_list,news_detail,news_by_category,news_create,create_report


urlpatterns = [
    path('',news_list,name="news-list"),
    path('<int:id>',news_detail,name="news-detail"),
    path('category/<int:category_id>/', news_by_category, name='news_by_category'),
    path('create/', news_create, name='news-create'),
    path('craete-report/',create_report,name="")
]
