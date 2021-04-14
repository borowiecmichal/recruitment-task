import hashlib
from operator import itemgetter
import requests
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class Task1View(APIView):
    def post(self, request):
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


class Task2View(APIView):
    def post(self, request):
        try:
            amount = float(request.data['buy'])
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        response = requests.get('https://bitbay.net/API/Public/BTCPLN/orderbook.json')
        offers = response.json()['asks']

        matching_offers = []
        best_offer = None
        for item in offers:
            if round(amount, 3) == round(float(item[1]), 3):
                matching_offers.append(item)
                price_per_amount = amount * float(item[0])
                if not best_offer or best_offer > price_per_amount:
                    best_offer = price_per_amount
        if best_offer:
            return Response(data={'price': best_offer}, status=status.HTTP_200_OK)
        else:
            return Response(data={'price': 'no offers for given amount'}, status=status.HTTP_204_NO_CONTENT)
