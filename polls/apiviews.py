from rest_framework.views import APIView
from rest_framework.response import Response, Serializer
from django.shortcuts import get_object_or_404
from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer


class PollList(APIView):
    def get(self, request):
        polls = Poll.objects.all()[:20]
        data = PollSerializer(polls, many=True).data
        return Response(data)


class PollDetail(APIView):
    def get(self, request, pk):
        polls = get_object_or_404(Poll, pk=pk)
        data = PollSerializer(polls).data
        return Response(data)
