from django.urls import path
from .views import PlanetList, PlanetDetail, CreatureList, CreatureDetail

# This file handles the 'map' for the creatures app.
# It tells Django which view should handle which URL path.
urlpatterns = [
    # When someone visits 'api/planets/', the PlanetList view takes over.
    path('planets/', PlanetList.as_view(), name='planet-list'),
    
    # When someone visits 'api/planets/1/', the PlanetDetail view takes over.
    path('planets/<int:pk>/', PlanetDetail.as_view(), name='planet-detail'),
    
    # When someone visits 'api/creatures/', the CreatureList view takes over.
    path('creatures/', CreatureList.as_view(), name='creature-list'),
    
    # When someone visits 'api/creatures/1/', the CreatureDetail view takes over.
    path('creatures/<int:pk>/', CreatureDetail.as_view(), name='creature-detail'),
]
