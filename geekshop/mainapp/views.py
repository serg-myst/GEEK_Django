from django.shortcuts import render
from django.conf import settings # В настройках пропишем путь до файла products.json
import json # модуль для преобразования текста в json и затем в словарь
import os # надо определить абсолютный путь к файлу products.json (через относительный не понимает. Говорит нет такого файла.).
# Для этого в settings.py добавил путь FILE_PRODUCTS

from mainapp.models import ProductCategory, Products

# Create your views here.
main_menu = [
    {'href': 'index', 'name': 'домой'},
    {'href': 'products', 'name': 'продукты'},
    {'href': 'contact', 'name': 'контакты'},
]

'''
links_menu = [
    {'href': 'products_all', 'name': 'все'},
    {'href': 'product_home', 'name': 'дом'},
    {'href': 'product_office', 'name': 'офис'},
    {'href': 'product_modern', 'name': 'модерн'},
    {'href': 'product_classic', 'name': 'классика'},
]
'''


def index(request):
    context = {
        'title': 'Магазин',
        'main_menu': main_menu,
    }

    return render(request, 'mainapp/index.html', context)


def products(request):

    links_menu = ProductCategory.objects.all().order_by('name')
    all_products = Products.objects.all()

    context = {
        'main_menu': main_menu,
        'links_menu': links_menu,
        'products': all_products,
    }

    return render(request, 'mainapp/products.html', context = context)


def contact(request):
    context = {
        'main_menu': main_menu,
    }

    return render(request, 'mainapp/contact.html', context)


def show_category_products(request, category_id=None):

    links_menu = ProductCategory.objects.all().order_by('name')

    if category_id in (3, None): # пока привяжимся к id категории "ВСЕ"
        all_products = Products.objects.all()
    else:
        all_products = Products.objects.filter(category=category_id)

    context = {
        'main_menu': main_menu,
        'links_menu': links_menu,
        'products': all_products,
        'active_category_id': category_id, # передаем для установки активного класса - active
    }

    return render(request, 'mainapp/products.html', context = context)


def get_products():

    filename = os.path.join(settings.FILE_PRODUCTS, 'products.json')

    with open(filename, 'r', encoding='utf-8') as f:
        data = json.loads(f.read().replace("'", '"'))
    return data

