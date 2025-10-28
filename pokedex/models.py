from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100, null=False)
    type = models.CharField(max_length=50, null=False)
    height = models.FloatField(null=False)
    weight = models.FloatField(null=False)
    picture = models.ImageField(upload_to='pokemon_pictures/', null=True, blank=True)

    def __str__(self):
        return self.name
