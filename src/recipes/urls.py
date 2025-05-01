from django.urls import path
from .views import home
from .views import RecipeListView
from .views import RecipeDetailView
from .views import recipe_search
app_name = 'recipes'
urlpatterns = [
    path('', home,),
    path('search/', recipe_search, name='search'),
    path('list/', RecipeListView.as_view(), name='recipe_list'),
    path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
   
]
