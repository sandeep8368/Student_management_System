from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import ItemViewset


router = DefaultRouter()
router.register(r'items',ItemViewset)
urlpatterns = [
    path('/', include(router.urls)),
]
