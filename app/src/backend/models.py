from django.db import models

# Create your models here.

class TypeName(models.Model):
    
    class Meta:
        db_table = 'typename'

    type_name =  models.CharField(max_length=25)

    def __str__(self):
        return self.type_name 


class Pokemon(models.Model):    
    
    class Meta:
        db_table = 'pokemon'

    number = models.IntegerField(verbose_name="Number")

    pokemon_name = models.CharField(verbose_name="Name", max_length=25)

    # type_name = models.ForeignKey("TypeName", on_delete=models.PROTECT)

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


class PokemonType(models.Model):

    class Meta:
        db_table = 'pokemon_type'

    pokemon_name = models.ForeignKey("Pokemon", on_delete=models.PROTECT)

    type_name = models.ForeignKey("TypeName", on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.pokemon.pokemon_name + ":" + self.typename.type_name