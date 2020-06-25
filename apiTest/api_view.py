from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import UserSerializer


class UserAPI(APIView):
    def post(self, request):
        serilizer = UserSerializer(data=request.data)
        if(serilizer.is_valid()):
            user = serilizer.save()
            return Response(serilizer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.error, status=status.HTTP_400_BAD_REQUEST)
