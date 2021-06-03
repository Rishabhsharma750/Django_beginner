from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloApiview(APIView):
    """Test Api view"""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apivew =[
            'Uses HTTP methods as functions (get,put,post,patch,delete)',
            'Is similar to the traditional Django view',
            'Gives you more control over your application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello!','an_apiview':an_apivew})

    def post(self,request):
        """Create a hello message with our name"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST

            )

    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        "Handle partial updating an object"
        return Response({'message':'PATCH'})

    def delete(self,request,pk=None):
        "Delete an object"
        return Response({'message':'DELETE'})