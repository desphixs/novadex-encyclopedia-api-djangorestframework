from django.urls import path
from .views import PlanetList

# This file handles the 'map' for the creatures app.
# It tells Django which view should handle which URL path.
urlpatterns = [
    # When someone visits 'api/planets/', the PlanetList view takes over.
    path('planets/', PlanetList.as_view(), name='planet-list'),
]
