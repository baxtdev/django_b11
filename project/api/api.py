from rest_framework.viewsets import ModelViewSet
from .serializers import News,NewsSerializer


class NewsModelViewset(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
