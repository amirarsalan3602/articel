from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import ArticleModel
from .serializers import ArticleSerializer
from django.shortcuts import get_object_or_404


class ArticleView(ViewSet):
    queryset = ArticleModel.objects.all()

    def list(self, request):
        ser_data = ArticleSerializer(instance=self.queryset, many=True).data
        return Response(data=ser_data, status=status.HTTP_200_OK)

    def create(self, request):
        ser_data = ArticleSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(data=ser_data, status=status.HTTP_201_CREATED)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        data = get_object_or_404(ArticleModel, pk=pk)
        ser_data = ArticleSerializer(instance=data, )
        return Response(data=ser_data.data)
