from django.shortcuts import render
from app.models import Item
from app.serializers import ItemSerializer
from rest_framework import viewsets
# Create your views here.

class ItemViewset(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
