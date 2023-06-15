from django.db import models

# Create your models here.
class Finch(models.Model):
    species = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)
    diet = models.CharField(max_length=100)
    lifespan = models.IntegerField()
    population = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.species} id:{self.id}'


finches = [
    {
        'species': 'Zebra Finch',
        'color': 'Gray',
        'size': 'Small',
        'habitat': 'Australia',
        'diet': 'Seeds',
        'lifespan': 5,
        'population': 'Common'
    },
    {
        'species': 'Goldfinch',
        'color': 'Yellow',
        'size': 'Small',
        'habitat': 'North America',
        'diet': 'Seeds, Insects',
        'lifespan': 10,
        'population': 'Stable'
    },
    {
        'species': 'Gouldian Finch',
        'color': 'Red, Green, Yellow',
        'size': 'Small',
        'habitat': 'Australia',
        'diet': 'Seeds, Insects',
        'lifespan': 6,
        'population': 'Endangered'
    },
    {
        'species': 'Purple Finch',
        'color': 'Red, Brown',
        'size': 'Medium',
        'habitat': 'North America',
        'diet': 'Seeds, Insects',
        'lifespan': 7,
        'population': 'Stable'
    },
    {
        'species': 'Society Finch',
        'color': 'White, Brown',
        'size': 'Small',
        'habitat': 'Domesticated',
        'diet': 'Seeds, Pellets',
        'lifespan': 7,
        'population': 'Common'
    },
    {
        'species': 'Crimson Finch',
        'color': 'Red',
        'size': 'Small',
        'habitat': 'Australia',
        'diet': 'Seeds, Insects',
        'lifespan': 6,
        'population': 'Stable'
    },
    {
        'species': 'European Goldfinch',
        'color': 'Red, Black, White',
        'size': 'Small',
        'habitat': 'Europe, Asia, Africa',
        'diet': 'Seeds, Insects',
        'lifespan': 12,
        'population': 'Stable'
    },
    {
        'species': 'Java Sparrow',
        'color': 'Gray',
        'size': 'Small',
        'habitat': 'Indonesia',
        'diet': 'Seeds',
        'lifespan': 7,
        'population': 'Endangered'
    },
    {
        'species': 'Bengalese Finch',
        'color': 'White, Brown',
        'size': 'Small',
        'habitat': 'Domesticated',
        'diet': 'Seeds, Insects',
        'lifespan': 5,
        'population': 'Common'
    },
    {
        'species': 'Red-cheeked Cordon-bleu',
        'color': 'Blue, Red',
        'size': 'Small',
        'habitat': 'Sub-Saharan Africa',
        'diet': 'Seeds, Insects',
        'lifespan': 5,
        'population': 'Stable'
    }
]