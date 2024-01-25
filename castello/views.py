from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.parsers import JSONParser

from .serializers import UserSerializer

from .models import User

from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse




class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


@csrf_exempt
def userApi(request, id=0):

    if request.method == 'GET':
        user = User.objects.all()
        user_serializer = UserSerializer(user, many=True)
        return JsonResponse(user_serializer.data, safe=False)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("User added successfully")
        return  JsonResponse("Fail to add user", safe=False)

    elif request.method == 'DELETE':
        user = User.objects.get(id=id)
        user.delete()
        return JsonResponse("User is deleted successfully", safe=False)

