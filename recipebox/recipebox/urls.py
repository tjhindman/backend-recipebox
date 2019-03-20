"""recipebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, auth
from django.contrib.auth import views as authViews
from django.urls import include, path, re_path
from . import views, settings

urlpatterns = [
    path('', views.RecipeListView, name='home'),
    path('login/', authViews.LoginView.as_view(), name='login'),
    path('logout/', authViews.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('author/', views.AuthorListView, name='authors'),
    path('author/<int:author_id>', views.AuthorView),
    path('recipe/<int:recipe_id>', views.RecipeView),
    path('recipe/new', views.RecipeCreateView),
    path('author/new', views.AuthorCreateView),
    path('accounts/', include('django.contrib.auth.urls')),
    # re_path(r'^login/$', views.UserLoginView, name='login'),
    # re_path(r'^logout/$', views.logout, name='logout'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
