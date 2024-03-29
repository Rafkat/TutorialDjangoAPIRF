from django.http import Http404
from rest_framework import status, request, mixins, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from snippets.models import Snippet
from snippets.serializers import SnippetsSerializer


class SnippetList(generics.ListCreateAPIView):
    """
    List all code snippets, or create a new snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetsSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve,update or delete a code snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetsSerializer

# Create your views here.
