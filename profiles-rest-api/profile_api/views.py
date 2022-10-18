from sys import api_version
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """
    Test API View
    """

    def get(self, request, format=None):
        """
        Returns a list of APIView features
        """
        an_apiview = [
            'Uses HHTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your app logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

