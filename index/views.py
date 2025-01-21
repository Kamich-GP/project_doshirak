from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import RegForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.views import View


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


# Регистрация
class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        return render(request, self.template_name)


    def post(self, request):
        form = request.POST

        if form:
            username = form.get('username')
            email = form.get('email')
            password = form.get('password2')

            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password).save()
            login(request, user)
            return redirect('/')


def search_product(request):
    if request.method == 'POST':
        get_product = request.POST.get('search_product')

        searched_product = Product.objects.filter(pr_name__iregex=get_product)

        if searched_product:
            context = {'products': searched_product}

            return render(request, 'result.html', context)
        else:
            return redirect('/')


