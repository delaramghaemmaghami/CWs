from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Recipe, Category
from pprint import pprint


def recipe_list(req):
    re = Recipe.objects.all()
    context ={
        'object_list':re,
       
    }
    #return render(req, 'recipe/recipe_list.html', {'recipes': re})
    return render(req, 'recipe/recipe_list.html', context)  #default
    return render(req, 'recipe/recipe_list.html', {'recipe_list': re})  # default new version

class RecipeList(ListView):
    model = Recipe  # re = Recipe.objects.all()
    template_name = "recipe/recipe_list_000.html"

    queryset = Recipe.objects.filter(recipe_name__startswith = "A").order_by("-id")

    # template_name or modelName/modelName_list.html
    # object_list or Recipe_list (modelName_list) or context_object_name
    #queryset = Recipe.objects.all()
    # queryset = Recipe.objects.filter(recipe_name__contains = "ch").order_by('-id')
    # queryset = Recipe.objects.filter(recipe_name__startswith = "A").order_by('-id')

    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     return super().get_context_data(**kwargs)

    #def get_context_data(self, **kwargs):
         #context = super().get_context_data(**kwargs)
         #pprint(dict(context.items()))
         #return context

    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)

        #context['test'] = "salam doustan :)"
        #return context


# def recipe_detail(req, id):
#     re = Recipe.objects.get(id=id)
#     return render(req, 'recipe/recipe_detail.html', {'recipes': re})

class RecipeDetail(DetailView):
    model = Recipe
    
