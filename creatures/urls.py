from django.urls import path
from .views import PlanetList, PlanetDetail

# This file handles the 'map' for the creatures app.
# It tells Django which view should handle which URL path.
urlpatterns = [
    # When someone visits 'api/planets/', the PlanetList view takes over.
    path('planets/', PlanetList.as_view(), name='planet-list'),
    
    # When someone visits 'api/planets/1/', the PlanetDetail view takes over.
    # The <int:pk> part tells Django to grab the number from the URL 
    # and pass it to our view as a variable called 'pk'.
    path('planets/<int:pk>/', PlanetDetail.as_view(), name='planet-detail'),
]
