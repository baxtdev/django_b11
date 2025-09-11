
from rest_framework import authentication, permissions,status
from rest_framework.views import APIView
from rest_framework.response import Response


class GETPOSTMixin:
    queryset = None
    serializer_class = None

    def get_queryset(self):
        return self.queryset.all()

    def get(self, request, format=None):
        query = self.get_queryset()
        news = self.serializer_class(query,many=True).data
        return Response(news,status=status.HTTP_200_OK)


    def post(self, request, format=None):
        news_data=request.data
        serializer_data = self.serializer_class(data=news_data,context={'request':request})
        
        if serializer_data.is_valid():
            data = serializer_data.save()
            return Response(serializer_data.data,status=status.HTTP_201_CREATED)

        return Response(serializer_data.errors)