from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Landing
from .serializers import LandingSerializer


# Create your views here.
@api_view(['GET'])
def index(request):
    try:
        schema = Landing.objects.filter(published=True).get()
        serializer = LandingSerializer(schema)
        return Response({"data": serializer.data})
    except Landing.DoesNotExist:
        raise Http404
