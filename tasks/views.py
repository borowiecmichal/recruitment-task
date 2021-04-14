import hashlib
from operator import itemgetter

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class Task1View(APIView):
    def post(self, request):
        print(request.data['data_list'])
        response_dict = {'result': []}
        try:
            for item in sorted(request.data['data_list'], key=itemgetter('second_name', 'first_name')):
                first_name = item['first_name']
                second_name = item['second_name']
                birth_date = item['birth_date']
                hash = hashlib.sha256(
                    (first_name + second_name + birth_date).encode('utf-8')).hexdigest()

                response_dict['result'].append(
                    {'first_name': first_name, 'second_name': second_name, 'birth_date': birth_date, 'hash': hash})

        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(data=response_dict, status=status.HTTP_200_OK)
