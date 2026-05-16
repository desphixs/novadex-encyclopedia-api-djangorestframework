from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Planet, Creature
from .serializers import PlanetSerializer, CreatureSerializer

# The PlanetList view is like a librarian for our Planets.
# It handles two main jobs:
# 1. Listing all the planets (GET) - like looking at a catalog.
# 2. Creating a new planet (POST) - like adding a new book to the shelf.
class PlanetList(APIView):
    # This method handles the GET request (fetching data).
    def get(self, request):
        # We grab every single planet from our database.
        planets = Planet.objects.all()
        
        # We give the planets to our translator (Serializer).
        # 'many=True' tells the translator: "I'm giving you a list of items, not just one."
        serializer = PlanetSerializer(planets, many=True)
        
        # We return the translated JSON data to the user.
        return Response(serializer.data)

    # This method handles the POST request (creating new data).
    def post(self, request):
        # We take the raw data the user sent us (request.data) 
        # and give it to our translator to check it out.
        serializer = PlanetSerializer(data=request.data)
        
        # We ask the translator: "Is this data valid? Does it follow our blueprint rules?"
        if serializer.is_valid():
            # If it's good, we save it to the database!
            serializer.save()
            
            # We return the newly created planet data with a '201 Created' status.
            # Analogy: This is like a store clerk handing you a receipt and saying "Order Complete!"
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # If the data was bad (e.g., missing a name), we return the error messages.
        # We also send a '400 Bad Request' status to let the user know they messed up.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
