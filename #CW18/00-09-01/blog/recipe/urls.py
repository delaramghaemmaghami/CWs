from django.urls import path
from .views import *

urlpatterns = [
    #path('', recipe_list, name="recipe_list"),
    path('', RecipeList.as_view(), name="recipe_list"),

    # path('<int:pk>', recipe_detail, name="recipe_detail"),
    path('<int:pk>/', RecipeDetail.as_view(), name="recipe_detail")
]