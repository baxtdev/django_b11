from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet

from blog.models import News,Category
from .serializers import NewsSerializer,CategorySerializer
from .permissions import IsOwnerPermissionOrReadOnly,IsAdminUser
from .paginations import StandardResultsSetPagination

class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'id'
    permission_classes = [IsOwnerPermissionOrReadOnly]
    pagination_class = StandardResultsSetPagination




class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'title'