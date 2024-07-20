from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404

# from utils.recipes.factory import make_recipe
from .models import Recipe

# Create your views here.


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    # return HttpResponse("Hello, World Django!")
    return render(
        request,
        "recipes/pages/home.html",
        context={'recipes': recipes}
    )


def category(request, category_id):
    # recipes = Recipe.objects.filter(
    #     category__id=category_id, is_published=True
    # ).order_by('-id')

    # if not recipes:
    #     raise Http404('Not found 🥲')

    # recipes = get_list_or_404(
    #   Recipe, category__id=category_id, is_published=True
    # )

    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id, is_published=True
        ).order_by('-id')
    )

    return render(
        request,
        'recipes/pages/category.html',
        context={
            'recipes': recipes,
            'title': f"{recipes[0].category.name} - Category | "
        }
    )


def contato(request):
    return HttpResponse("Contato: Django!")


def recipe(request, id):
    # recipe = Recipe.objects.filter(
    #     pk=id, is_published=True
    # ).order_by('-id').first()

    recipe = get_object_or_404(Recipe, pk=id, is_published=True)

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })
