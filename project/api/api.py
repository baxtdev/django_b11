from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet,GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from blog.models import News,Category
from .serializers import NewsSerializer,\
    CategorySerializer,\
    RegisterSerializer,CustomUser

from .permissions import IsOwnerPermissionOrReadOnly,IsAdminUser
from .paginations import StandardResultsSetPagination


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'id'
    permission_classes = [IsOwnerPermissionOrReadOnly]
    pagination_class = StandardResultsSetPagination


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'title'


class UserRegisterViewSet(CreateModelMixin,GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer


class AcccountProfileViewSet(GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]

    def get(self,request,format=None,*args,**kwargs):
        user = request.user
        user_data = self.serializer_class(instance=user,
                                          context={'request':request}).data
        return Response(user_data)

    
    def put(self, request, *args, **kwargs):
        pass
    
    def patch(self, request, *args, **kwargs):
        pass        
    
    def delete(self, request, *args, **kwargs):
        pass