from django.core import serializers
import json
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from api.models import Hero


def heroes(request):
    if request.method == 'GET':
        heroes = Hero.objects.values()
        heroes = list(heroes)
        # posts_serialized = serializers.serialize('json', heroes, ensure_ascii=False)
        return JsonResponse(heroes,safe=False)
    elif request.method == 'POST':
        received_json_data = json.loads(request.body)
        name = received_json_data['name']
        hero = Hero(name=name)
        hero.save()
        hero_dict = model_to_dict(hero)
        return JsonResponse(hero_dict, safe=False)


def hero(request,**kwargs):
    if request.method == 'GET':
        hero = Hero.objects.get(pk=kwargs['id'])
        hero_dict = model_to_dict(hero)
        return JsonResponse(hero_dict, safe=False)
    elif request.method == 'POST':
        received_json_data = json.loads(request.body)
        name = received_json_data['name']
        hero = Hero.objects.get(pk=kwargs['id'])
        hero.name = name
        hero.save()
        hero_dict = model_to_dict(hero)
        return JsonResponse(hero_dict, safe=False)


def delete_hero(request,**kwargs):
    if request.method == 'POST':
        hero = Hero.objects.get(pk=kwargs['id'])
        hero.delete()
        hero_dict = model_to_dict(hero)
        return JsonResponse(hero_dict, safe=False)