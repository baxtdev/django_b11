
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions,status


from blog.models import News,Category
from .serializers import NewsSerializer,CategorySerializer
from .mixins import GETPOSTMixin

class NewsListAPIView(GETPOSTMixin,APIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    


class NewsDetailAPIView(APIView):

    def get_object(self,pk):
        return get_object_or_404(News,pk=pk)

    def get(self,request,pk,format=None,*args,**kwargs):
        news = self.get_object(pk)
        news_data = NewsSerializer(news).data
        return Response(news_data,status=status.HTTP_200_OK)


    def delete(self,request,pk,format=None,*args,**kwargs):
        news = self.get_object(pk)
        news.delete()
        return Response({"detail":f"Object news with id {news.id} was deleted"},status=status.HTTP_204_NO_CONTENT)

    def put(self,request,pk,format=None,*args,**kwargs):
        news = self.get_object(pk)
        news_data = NewsSerializer(news,data=request.data,context={'request':request})
        if news_data.is_valid():
            news_data.save()
            return Response(news_data.data) 
        
        return Response(news_data.errors)


class CategoryAPIVIew(GETPOSTMixin,APIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer