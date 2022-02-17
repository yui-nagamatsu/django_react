from math import atanh
from django.db import models

# Create your models here.

# perとnatはよくわからないので、numberで一括りにした。
# "LK/GK", "EV Worth", "EXPV"は不明なので、無視。
class Pokemon_Models(models.Model):
    
    
    class Meta:
        db_table = 'Pokemon'

    pokemon_number = models.CharField(
        verbose_name='Number',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    pokemon_name = models.CharField(
        verbose_name='Name',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    hp = models.CharField(
        verbose_name='HP',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    atk = models.CharField(
        verbose_name='Attack',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    dfs = models.CharField(
        verbose_name='Defense',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    spatk = models.CharField(
        verbose_name='Special Attack',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    spdfs = models.CharField(
        verbose_name='Special Defense',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    spe = models.CharField(
        verbose_name='Speed',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    total = models.CharField(
        verbose_name='Total',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    type_1 = models.CharField(
        verbose_name='Type I',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    type_2 = models.CharField(
        verbose_name='Type II',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    tier = models.CharField(
        verbose_name='Tier',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    ability_1 = models.CharField(
        verbose_name='Ability I',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    ability_2 = models.CharField(
        verbose_name='Ability II',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    hidden_ability = models.CharField(
        verbose_name='Hidden Ability',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    weight = models.CharField(
        verbose_name='Weight',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    color = models.CharField(
        verbose_name='Color',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    hatch = models.CharField(
        verbose_name='Hatch',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    gender = models.CharField(
        verbose_name='Gender',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    egg_group_1 = models.CharField(
        verbose_name='Egg Group I',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )
    egg_group_2 = models.CharField(
        verbose_name='Egg Group II',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    catch = models.CharField(
        verbose_name='Catch',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    exp = models.CharField(
        verbose_name='EXP',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    evolve = models.CharField(
        verbose_name='Evolve',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    def __str__(self):
        return self.pokemon_number