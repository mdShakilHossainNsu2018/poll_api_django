# from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response, Serializer
from django.shortcuts import get_object_or_404
from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer


class PollList(generics.ListAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()


class PollDetail(generics.RetrieveDestroyAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()


class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class CreateVote(generics.CreateAPIView):
    serializer_class = VoteSerializer
