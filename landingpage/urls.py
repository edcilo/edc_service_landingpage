from django.urls import path

from . import views


# namespace
app_name = 'landingpage'

# urls
urlpatterns = [
    path('', views.index, name='index'),
    path('api/v1/', views.published_schema, name='published_schema'),
]
