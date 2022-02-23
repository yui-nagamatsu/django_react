from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from backend.models import Pokemon

class IndexView(generic.ListView):
    template_name = 'backend/index.html'
    context_object_name = 'random_featured_pokemon'
    def get_queryset(self):
        return Pokemon.objects.order_by('?')[:10]

#class DetailView(generic.DetailView):
#    model = Pokemon
#    template_name = 'backend/detail.html'
#    def get_object(self):
#        return Pokemon.objects.get('__all__')


class DetailView(generic.DetailView):
    model = Pokemon
    template_name = 'backend/detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        return obj