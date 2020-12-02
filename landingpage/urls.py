from django.urls import path

from . import views


# namespace
app_name = 'landingpage'

# urls
urlpatterns = [
    path('api/v1/', views.index, name='index'),
]
