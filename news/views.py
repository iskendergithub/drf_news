from django.shortcuts import render
from .serializers import NewsSeriallizer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import News


@api_view(['GET'])
def my_news_view(request):
    data = {
        'text': 'Hello, my frontend !'
    }
    return Response(data)


@api_view(['GET'])
def news_list_view(request):
    news_list = News.objects.all()
    serializer = NewsSeriallizer(news_list, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def news_detail_view(request, id):
    news_list = News.objects.get(id=id)
    serializer = NewsSeriallizer(news_list, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def news_create_view(request):
    serializer = NewsSeriallizer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response({"Created: News is created !"})


@api_view(['POST'])
def news_update_view(request, id):
    news_list = News.objects.get(id=id)
    serializer = NewsSeriallizer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def news_delete_view(request, id):
    news_list = News.objects.get(id=id)
    news_list.delete()

    return Response({"info": "News was deleted"})