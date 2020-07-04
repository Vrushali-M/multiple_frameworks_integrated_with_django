from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import task_serializer

from .models import task as task_
# Create your views here.

@api_view(['GET'])

def todo_app(request):
    
    api_urls = {
        'List' : '/tasks/',
        'Detail' : '/detail/<str:pk>',
        'Create' : '/create/',
        'Update' : '/update/<str:pk>',
        'Delete' : '/delete/<str:pk>',
    }


    return Response(api_urls)


@api_view(['GET'])
def task_list(request):

    tasks = task_.objects.all()
    serializer = task_serializer(tasks, many= True)

    return Response(serializer.data)

@api_view(['GET'])
def task_detail(request, pk):

    tasks = task_.objects.get(id = pk)
    serializer = task_serializer(tasks, many= False)

    return Response(serializer.data)

@api_view(['POST'])
def task_create(request):
    
    serializer = task_serializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def task_update(request, pk):

    task = task_.objects.get(id = pk)    
    serializer = task_serializer(instance = task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def task_delete(request, pk):

    task = task_.objects.get(id = pk)    
    task.delete()
    return Response("Item successfully deleted")

def manifest(request):
    console.log("In manifest", os.join(BASE_DIR))
    return (open('manifest.json'))