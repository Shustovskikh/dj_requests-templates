from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'roast_cat': {
        'кошка, кг': 0.2,
        'масло, г': 0.02,
        'соль, г': 0.03,
        'перец, г': 0.01,
    }
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def index_view(request):
    dishes = list(DATA.keys())
    context = {'dishes': dishes}
    return render(request, 'calculator/index.html', context)

def recipe_view(request, dish_name):
    recipe = DATA.get(dish_name)
    if recipe is not None:
        servings = request.GET.get('servings', 1)
        try:
            servings = int(servings)
            recipe = {ingredient: quantity * servings for ingredient, quantity in recipe.items()}
        except ValueError:
            pass
        context = {'recipe': recipe}
    else:
        context = {
            'recipe': {},
            'error_message': 'Рецепт не найден'
        }
    return render(request, 'calculator/index.html', context)

def recipe_list_view(request):
    recipes = list(DATA.keys())
    context = {'recipes': recipes}
    return render(request, 'calculator/recipe_list.html', context)