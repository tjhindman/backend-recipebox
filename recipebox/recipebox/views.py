from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.http import Http404
from django.urls import reverse
from django.shortcuts import redirect, render
from .models import Author, Recipe, User
from .forms import AuthorForm, RecipeForm


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


def AuthorListView(req):
    authors = Author.objects.all()
    return render(req, 'author_list.html', {
        'authors': authors,
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


@login_required(login_url='/accounts/login', redirect_field_name='home')
def RecipeCreateView(req):

    if req.method == "POST":
        form = RecipeForm(req, req.user.is_staff)

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
        form = RecipeForm(req, req.user.is_staff)

    return render(req, 'recipe_create.html', {'recipeForm': form})


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


@login_required(login_url='/accounts/login', redirect_field_name='home')
def EditRecipeView(UpdateView):
    model = Recipe
    fields = ['title', 'description', 'total_time', 'instructions']
    template_name_suffix = '_create'


# def UserLoginView(req):
#     if req.method == 'POST':
#         username = req.POST['username']
#         password = req.POST['password']
#         user = authenticate(req, username=username, password=password)

#         if user is not None:
#             login(req, user)
#             return redirect(reverse('home'))
#         else:
#             return Http404('User does not exist')
#     else:
#         form = LoginForm
#         return render(req, 'authentication/login.html', {'loginView': form})


# def logout(req):
#     pass


# def signup(req):
#     pass
