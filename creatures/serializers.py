from rest_framework import serializers
from .models import Planet, Creature

# Serializers are the translators of our API.
# Think of a Serializer like a bilingual translator at a peace summit. 
# One side speaks 'Python/Database' and the other side speaks 'JSON/Internet'.
# The Serializer makes sure they can understand each other.

class PlanetSerializer(serializers.ModelSerializer):
    # This class tells the serializer which model to use and which fields to include.
    class Meta:
        model = Planet
        # '__all__' means "grab every field we defined in the model".
        fields = '__all__'

class CreatureSerializer(serializers.ModelSerializer):
    # Here is the cool part: Nesting!
    # By defining 'planet' here, we tell DRF to include all the planet's details 
    # (name, climate) inside the creature's JSON, instead of just a raw ID number.
    # 'read_only=True' means we only want to see these details when reading (GET).
    # When creating a creature, we will handle the planet ID differently.
    planet = PlanetSerializer(read_only=True)

    class Meta:
        model = Creature
        fields = '__all__'
