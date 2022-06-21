from urllib import response
from itsdangerous import Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from mlmodel.models import Mlmodel
from .serializers import DangerSerializer
from mlmodel.serializers import MlmodelSerializer
from .models import Danger
from api import serializers
@api_view(['GET'])
# Create your views here.

def getRoutes(request):
    
    routes = [
    {
         'endpoint' : '/danger',
         'method' : 'GET',
         'body' : None,
         'description' : 'return data of admins',

    },
    {
         'endpoint' : '/danger/users',
         'method' : 'GET',
         'body' : None,
         'description' : 'return data of users',

   },
     {
         'endpoint' : '/danger/create',
         'method' : 'POST',
         'body' : None,
         'description' : 'create new user',

   },
   {
         'endpoint' : '/danger/"userid"/update',
         'method' : 'PUT',
         'body' : None,
         'description' : 'update user data',

   },
   {
         'endpoint' : '/danger/"userid"/delete',
         'method' : 'DELETE',
         'body' : None,
         'description' : 'delete user data',
   },
]
    return Response (routes)

@api_view(['GET'])
def getDanger(request):
     danger = Danger.objects.all()
     Serializer = DangerSerializer(danger, many=True)
     return Response(Serializer.data)

@api_view(['GET'])
def getDanger0(request, pk):
     danger0 = Danger.objects.get(id=pk)
     Serializer = DangerSerializer(danger0, many=False) 
     return Response(Serializer.data)  

@api_view(['POST'])
def createDanger(request):
     data = request.data
     danger = Danger.objects.create(
          body=data['body']
     )
     serializer = DangerSerializer(danger, many= False)
     return Response(serializer.data)


@api_view(['PUT'])
def updateDanger(request, pk):
     data = request.data
     danger = Danger.objects.get(id=pk)
     serializer = DangerSerializer(danger, data=request.data)
     if serializer.is_valid():
          serializer.save()
     return Response(serializer.data) 


@api_view(['DELETE'])
def deleteDanger(request, pk):
     danger = Danger.objects.get(id=pk)
     danger.delete()
     return Response('Danger was deleted')

@api_view(['GET'])
def mlmodel(request, pk):
     mlmodel = Mlmodel.objects.get(id=pk)
     Serializer = MlmodelSerializer(mlmodel, many=False) 
     return Response(Serializer.data)    