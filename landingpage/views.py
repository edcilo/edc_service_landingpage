from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.http import Http404
from django.shortcuts import redirect
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Landing
from .serializers import LandingSerializer

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
REDIRECT_TO = getattr(settings, 'HOME_REDIRECT_TO')


# Create your views here.
@api_view(['GET'])
def index(request):
    return redirect(REDIRECT_TO)


@cache_page(CACHE_TTL, key_prefix="landing_view")
@api_view(['GET'])
def published_schema(request):
    try:
        lang = request.GET['lang'] if 'lang' in request.GET else None
        schema = Landing.objects.filter(published=True).get()

        if lang is not None and lang not in schema.schema:
            raise Http404

        if lang is not None:
            schema.schema = schema.schema[lang]

        serializer = LandingSerializer(schema)
        return Response({"data": serializer.data})
    except Landing.DoesNotExist:
        raise Http404
