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
        
        # We also send a '400 Bad Request' status to let the user know they messed up.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# The PlanetDetail view is like a specific store manager handling one single product.
# This view handles operations on a specific planet using its ID (pk).
class PlanetDetail(APIView):
    # This helper method saves us from writing the same try/except block 3 times.
    # Analogy: This is like a security guard checking if a specific room exists 
    # before letting you try to enter, clean, or demolish it.
    def get_object(self, pk):
        try:
            return Planet.objects.get(pk=pk)
        except Planet.DoesNotExist:
            return None

    # Retrieve a single planet (GET)
    def get(self, request, pk):
        planet = self.get_object(pk)
        if planet is None:
            # If the planet doesn't exist, we send back a 404.
            # Analogy: This is like looking for a book in a library that isn't in the catalog.
            return Response({"error": "Planet not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PlanetSerializer(planet)
        return Response(serializer.data)

    # Update a single planet (PUT)
    def put(self, request, pk):
        planet = self.get_object(pk)
        if planet is None:
            return Response({"error": "Planet not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # We pass the 'planet' instance we found AND the new data from the user.
        # This tells the serializer to update the existing record instead of creating a new one.
        serializer = PlanetSerializer(planet, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a single planet (DELETE)
    def delete(self, request, pk):
        planet = self.get_object(pk)
        if planet is None:
            return Response({"error": "Planet not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # We permanently remove the planet from the database.
        # Analogy: This is like deleting a file from your computer's trash bin.
        planet.delete()
        
        # We return a 204 No Content because the planet is gone!
        return Response(status=status.HTTP_204_NO_CONTENT)

# The CreatureList view is like an explorer's logbook.
# It allows us to see all discovered creatures and log new ones.
class CreatureList(APIView):
    # This method handles the GET request (listing creatures).
    def get(self, request):
        # We fetch all creatures from our galactic database.
        creatures = Creature.objects.all()
        
        # We use the CreatureSerializer to translate them into JSON.
        # Remember: This will include the full planet details because of our nesting!
        serializer = CreatureSerializer(creatures, many=True)
        
        return Response(serializer.data)

    # This method handles the POST request (adding a new creature).
    def post(self, request):
        # We give the incoming data to the translator.
        serializer = CreatureSerializer(data=request.data)
        
        # We check if the name, danger level, etc., are all valid.
        if serializer.is_valid():
            # IMPORTANT: Because the 'planet' field in our serializer is read-only 
            # (to show the full object on GET), we have to tell Django exactly 
            # which planet ID to link this new creature to.
            # We grab 'planet_id' from the raw data sent by the user.
            planet_id = request.data.get('planet_id')
            
            # We save the creature and manually 'stitch' it to the planet.
            # Analogy: This is like a doctor filling out a birth certificate (creature) 
            # and manually writing down the hospital's address (planet ID).
            serializer.save(planet_id=planet_id)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # If the user forgot a field or sent bad data, we let them know.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
