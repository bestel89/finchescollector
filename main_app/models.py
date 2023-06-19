from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})

# Create your models here.
class Finch(models.Model):
    species = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)
    diet = models.CharField(max_length=100)
    lifespan = models.IntegerField()
    population = models.CharField(max_length=100)
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return f'{self.species} id:{self.id}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id}) #Django equivalent of URL template tag

class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )

    finch = models.ForeignKey(
        Finch,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"({self.get_meal_display()} on {self.date})"
    
    class Meta:
        ordering = ['-date']