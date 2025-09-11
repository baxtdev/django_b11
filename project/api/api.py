
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions,status


from blog.models import News,Category
from .serializers import NewsSerializer

class NewsListAPIView(APIView):
    def get(self, request, format=None):
        news = NewsSerializer(News.objects.all(),many=True).data
        return Response(news,status=status.HTTP_200_OK)


    def post(self, request, format=None):
        news_data=request.data
        {
            "title":"asd",
            "category":1
        }
        serializer_data = NewsSerializer(data=news_data,context={'request':request})
        
        if serializer_data.is_valid():
            data = serializer_data.save()
            return Response(serializer_data.data,status=status.HTTP_201_CREATED)

        return Response(serializer_data.errors)
    


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