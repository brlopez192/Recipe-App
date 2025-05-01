from django.urls import path
from .views import home
from .views import RecipeListView
from .views import RecipeDetailView
from .views import recipe_search
from .views import add_recipe
app_name = 'recipes'
urlpatterns = [
    path('homescreen', home, name='home'),
    path('search/', recipe_search, name='search'),
    path('add/', add_recipe, name='add'),
    path('list/', RecipeListView.as_view(), name='recipe_list'),
    path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
   
]
