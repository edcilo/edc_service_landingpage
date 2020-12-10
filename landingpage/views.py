from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.http import Http404
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Landing
from .serializers import LandingSerializer

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


# Create your views here.
@cache_page(CACHE_TTL, key_prefix="landing_view")
@api_view(['GET'])
def index(request):
    try:
        schema = Landing.objects.filter(published=True).get()
        serializer = LandingSerializer(schema)
        return Response({"data": serializer.data})
    except Landing.DoesNotExist:
        raise Http404
