from django.db import models

# Create your models here.

class Pokemon(models.Model):    
    
    class Meta:
        db_table = 'pokemon'

    number = models.IntegerField(verbose_name="Number")

    name = models.CharField(verbose_name="Name", max_length=25)

    type1 = models.CharField(verbose_name="Type1", max_length=25)

    type2 = models.CharField(verbose_name="Type2", max_length=25, default='')

    heart_point = models.IntegerField(verbose_name="HP")

    attack = models.IntegerField(verbose_name="Attack")

    defense = models.IntegerField(verbose_name="Defense")

    special_attack = models.IntegerField(verbose_name="Special Attack")

    special_defense = models.IntegerField(verbose_name="Special Defense")

    speed = models.IntegerField(verbose_name="Speed")

    generation = models.IntegerField(verbose_name="The generation in which this pokemon first appears.")

    is_legendary = models.BooleanField(verbose_name="If this pokemon is legendary or not.")

    def __str__(self):
        return self.name