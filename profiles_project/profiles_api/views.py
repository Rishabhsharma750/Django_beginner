from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiview(APIView):
    """Test Api view"""

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apivew =[
            'Uses HTTP methods as functions (get,put,post,patch,delete)',
            'Is similar to the traditional Django view',
            'Gives you more control over your application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello!','an_apiview':an_apivew})