import json
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import generics

from election.models import Party
from election.serialzers import PartySerialzer

# class GetListParties(APIView):
#     def get(self, request):
#         parties = Party.objects.all()
#         serialzer = PartySerialzer(parties, many=True)
#         return JsonResponse(serialzer.data, safe=False)

class GetListParties(generics.ListCreateAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerialzer


class GetDetailParty(generics.RetrieveUpdateDestroyAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerialzer