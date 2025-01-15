from django.shortcuts import render
from .models import Product, Category


# Create your views here.
# Главная страница
def home_page(request):
    # Получаем информацию из БД
    products = Product.objects.all()
    categories = Category.objects.all()
    # Отправляем данные на фронт
    context = {'products': products, 'categories': categories}

    return render(request, 'home.html', context)

# Страница выбранной категории
def category_page(request, pk):
    # Вытаскиваем выбранную категорию
    category = Category.objects.get(id=pk)
    # Фильтруем товары по выбранной категории
    products = Product.objects.filter(pr_category=category)
    # Отправляем данные на фронт
    context = {'category': category, 'products': products}

    return render(request, 'category.html', context)


# Страница выбранного продукта
def product_page(request, pk):
    # Вытаскиваем выбранный продукт
    product = Product.objects.get(id=pk)
    # Передаем данные на фронт
    context = {'product': product}

    return render(request, 'product.html', context)

