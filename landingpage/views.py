from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import Landing
from .serializers import LandingSerializer


# Create your views here.
@api_view(['GET'])
def index(request):
    schema = Landing.objects.filter(published=True).get()
    serializer = LandingSerializer(schema)
    return JsonResponse(serializer.data, safe=True)
