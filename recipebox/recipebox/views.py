from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.urls import reverse
from django.shortcuts import redirect, render
from .models import Author, Recipe, User
from .forms import AuthorForm, RecipeForm


@staff_member_required
def AuthorCreateView(req):

    if req.method == "POST":
        form = AuthorForm(req.POST)

        if form.is_valid():
            d = form.cleaned_data
            user = User.objects.create_user(d['username'])
            Author.objects.create(
                user=user,
                bio=d['bio'])
            return redirect(reverse('home'))

    else:
        form = AuthorForm
        return render(req, 'author_create.html', {'authorForm': form})


def AuthorListView(req):
    authors = Author.objects.all()
    return render(req, 'author_list.html', {
        'authors': authors,
    })


def AuthorView(req, author_id):
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


def RecipeView(req, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(req, 'recipe_detail.html', {
        'recipe': recipe,
    })


def RecipeListView(req):
    recipes = Recipe.objects.all()
    return render(req, 'recipe_list.html', {
        'recipes': recipes,
    })


@staff_member_required
def RecipeCreateView(req):

    if req.method == "POST":
        form = RecipeForm(req.POST)

        if form.is_valid():
            d = form.cleaned_data
            Recipe.objects.create(
                author_id=d['author'],
                title=d['title'],
                description=d['description'],
                total_time=d['total_time'],
                instructions=d['instructions'])
            return redirect(reverse('home'))
    else:
        form = RecipeForm
        return render(req, 'recipe_create.html', {'recipeForm': form})
