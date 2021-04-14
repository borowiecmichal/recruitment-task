from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class Task1View(APIView):
    def post(self, request):
        print(request.data.data_list)
        return Response(status=status.HTTP_200_OK)
