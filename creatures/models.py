from django.db import models

# The Planet model represents a home world for our aliens.
# Think of this like a 'Category' in a blog, or a 'Department' in a store.
class Planet(models.Model):
    # 'name' stores the name of the planet (e.g., "Mars", "Vel'kara").
    name = models.CharField(max_length=100)
    
    # 'climate' describes the environment (e.g., "Arid", "Jungle").
    # Analogy: This is like describing the terrain of a game level.
    climate = models.CharField(max_length=100)

    # This method tells Django how to display this object in the admin panel.
    def __str__(self):
        return self.name

# The Creature model represents a specific alien species.
class Creature(models.Model):
    # 'name' is the name of the species (e.g., "Gorgon", "Space Whale").
    name = models.CharField(max_length=100)
    
    # 'description' is for long-form text about the species.
    description = models.TextField()
    
    # 'danger_level' is a simple number from 1 to 10.
    danger_level = models.IntegerField()
    
    # 'planet' is a ForeignKey, creating a One-to-Many relationship.
    # Analogy: This is like a child holding their parent's hand. 
    # Many children (creatures) can hold the hand of one parent (planet).
    # 'on_delete=models.CASCADE' means if the planet is destroyed, 
    # all creatures living there are also removed from the database.
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name='creatures')

    # Just like before, this helps us see the name in the admin panel.
    def __str__(self):
        return self.name
