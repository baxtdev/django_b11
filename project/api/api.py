from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet

from blog.models import News,Category
from .serializers import NewsSerializer,CategorySerializer


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'id'


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'title'