from django.shortcuts import render
from .models import Product


# Create your views here.
def home_page(request):
    # Получаем информацию из БД
    products = Product.objects.all()
    # Отправляем данные на фронт
    context = {'products': products}

    return render(request, 'home.html', context)
