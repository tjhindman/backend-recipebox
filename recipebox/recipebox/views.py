from django.http import Http404
from django.shortcuts import render
from recipebox.models import Author, Recipe


def index_home(req):
    recipes = Recipe.objects.all()
    return render(req, 'recipe_list.html', {
        'recipes': recipes,
    })


def authors(req):
    authors = Author.objects.all()
    return render(req, 'author_list.html', {
        'authors': authors,
    })


def author(req, author_id):
    try:
        author = Author.objects.get(id=author_id)
        recipes = Recipe.objects.filter(author_id=author_id)
    except author.DoesNotExist:
        raise Http404('User does not exist')
    except recipes.DoesNotExist:
        return render(req, 'author_detail.html', {'author': author})

    return render(req, 'author_detail.html', {
        'author': author,
        'recipes': recipes,
    })


def recipe(req, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(req, 'recipe_detail.html', {
        'recipe': recipe
    })
