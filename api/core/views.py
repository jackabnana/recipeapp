from rest_framework import viewsets
from .serializers import RecipeSerializer
from .models import Recipe
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view



class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()