from django.http import FileResponse, JsonResponse, HttpResponseRedirect, HttpResponse, Http404, StreamingHttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
import datetime, json
from django.core.serializers.json import DjangoJSONEncoder
from django.template.loader import get_template
from .models import *
from django.conf import settings
from django.conf.urls.static import static
from APP.forms import *

class Producti:   
    __max_id = 0

    def __init__(self, name: str,  
                 ves: int,
                 category:str,
                 price: int,
                 srok_godnosti: int, 
                 volume: int):     
        self.id = Producti.__max_id
        self.name = name
        self.ves = ves
        self.category = category
        self.price = price
        self.godnost = srok_godnosti
        self.volume = volume
        Producti.__max_id += 1



    def __str__(self):
        return (
              f'ID: {self.id}<br>'   
            + f'Name: {self.name}<br>'
            + f'Ves: {self.ves} грамм<br>'
            + f'Category: {self.category}<br>'
            + f'Price: {self.price} рублей<br>'
            + f'Godnost: {self.godnost} дней<br>'
            + f'Volume: {self.volume} миллилитров<br>'
        )

products = [Producti('Milk', 1500, 'Dairy products', 67, 7, 1000),
            Producti('Butter', 450, 'Dairy products', 327, 21, 200),
            Producti('Cheese', 300, 'Dairy products', 423, 13, 400),
            Producti('Chips', 150, 'Snacks', 103, 100, 500),
            Producti('Crispy fish', 250, 'Snacks', 72, 120, 300),
            Producti('Crackers', 500, 'Snacks', 149, 99, 600),
            Producti('Lemon', 40, 'Сitrus fruit', 17, 62, 32),
            Producti('Grapefruit', 300, 'Сitrus fruit', 64, 15, 400),
            Producti('Tangerine', 16, 'Citrus fruit', 12, 13, 23),
            Producti('Chicken', 1600, 'Meat', 478, 4, 612),
            Producti('', '', '', '', '', '')]


def products_view(request: HttpResponse):
    if request.method == 'GET':
        category = request.GET.get('category', None)
        print(repr(category), repr(products[-1].category))
        return HttpResponse('<br><br>'.join(str(product) for product in products
                                        if category is None
                                        or category == product.category))


    if request.method == 'POST':
        body = [element.strip() for element in
                request.body.decode('UTF-8').split('<br>')]

        products.append(Producti(
            name = body[0],
            category = body[1], 
            price = int(body[2]),
            ves = int(body[3]),
            volume = int(body[4]),
            godnost = int(body[5])
         )) 

        return HttpResponse(str(products[-1]), status=200)
    
    return HttpResponse(status=405)


def product_view(request: HttpResponse, id: int):
    filtered = [product for product in products if product.id == id]
    
    if request.method == 'GET':      #задание 3
        if int(id) > 10:             #задание 3
            raise Http404            #задание 3

    if len(filtered) == 0:
        return HttpResponse(status=404)


    product = filtered[0]

    if request.method == 'GET':
        if product.name == '':
            return HttpResponseRedirect(reverse('products'))

        return HttpResponse(str(product))
    
    return HttpResponse(status=405)


class ProductEncoder_2(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Producti):
            return [{'Name':obj.name, 'Ves':obj.ves, 'Category':obj.category, 'Price':obj.price, 'Godnost':obj.godnost, 'Volume':obj.volume}]
        return super().default(obj)

class ProductEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Producti):
            return [{'Name':obj.name, 'Ves':obj.ves, 'Category':obj.category, 'Price':obj.price, 'Godnost':obj.godnost, 'Volume':obj.volume}, 
                    {obj.name:'Name', obj.ves:'Ves', obj.category:'Category', obj.price:'Price', obj.godnost:'Godnost', obj.volume:'Volume'}]
        return super().default(obj)

milk = Producti('Milk', 1500, 'Dairy products', 67, 7, 1000)
chips = Producti('Chips', 150, 'Snacks', 103, 100, 500)
butter = Producti('Butter', 450, 'Dairy products', 327, 21, 200)
lemon = Producti('Lemon', 40, 'Сitrus_fruit', 17, 62, 32)
chipsy_fish = Producti('Crispy fish', 250, 'Snacks', 72, 120, 300)
creckers = Producti('Crackers', 500, 'Snacks', 149, 99, 600)
grapefruit = Producti('Grapefruit', 300, 'Сitrus fruit', 64, 15, 400)
tangerine = Producti('Tangerine', 16, 'Citrus fruit', 12, 13, 23)
chicken = Producti('Chicken', 1600, 'Meat', 478, 4, 612)
cheese = Producti('Cheese', 300, 'Dairy products', 423, 13, 400)

milk_slov = [{'Name':milk.name, 'Ves':milk.ves, 'Category':milk.category, 'Price':milk.price, 'Godnost':milk.godnost, 'Volume':milk.volume}, 
            {milk.name:'Name', milk.ves:'Ves', milk.category:'Category', milk.price:'Price', milk.godnost:'Godnost', milk.volume:'Volume'}]

chips_slov = [{'Name':chips.name, 'Ves':chips.ves, 'Category':chips.category, 'Price':chips.price, 'Godnost':chips.godnost, 'Volume':chips.volume}, 
            {chips.name:'Name', chips.ves:'Ves', chips.category:'Category', chips.price:'Price', chips.godnost:'Godnost', chips.volume:'Volume'}]

butter_slov = [{'Name':butter.name, 'Ves':butter.ves, 'Category':butter.category, 'Price':butter.price, 'Godnost':butter.godnost, 'Volume':butter.volume}, 
            {butter.name:'Name', butter.ves:'Ves', butter.category:'Category', butter.price:'Price', butter.godnost:'Godnost', butter.volume:'Volume'}]

lemon_slov = [{'Name':lemon.name, 'Ves':lemon.ves, 'Category':lemon.category, 'Price':lemon.price, 'Godnost':lemon.godnost, 'Volume':lemon.volume}, 
            {lemon.name:'Name', lemon.ves:'Ves', lemon.category:'Category', lemon.price:'Price', lemon.godnost:'Godnost', lemon.volume:'Volume'}]

chipsy_fish_slov = [{'Name':chipsy_fish.name, 'Ves':chipsy_fish.ves, 'Category':chipsy_fish.category, 'Price':chipsy_fish.price, 'Godnost':chipsy_fish.godnost, 'Volume':chipsy_fish.volume}, 
            {chipsy_fish.name:'Name', chipsy_fish.ves:'Ves', chipsy_fish.category:'Category', chipsy_fish.price:'Price', chipsy_fish.godnost:'Godnost', chipsy_fish.volume:'Volume'}]

creckers_slov = [{'Name':creckers.name, 'Ves':creckers.ves, 'Category':creckers.category, 'Price':creckers.price, 'Godnost':creckers.godnost, 'Volume':creckers.volume}, 
            {creckers.name:'Name', creckers.ves:'Ves', creckers.category:'Category', creckers.price:'Price', creckers.godnost:'Godnost', creckers.volume:'Volume'}]

grapefruit_slov = [{'Name':grapefruit.name, 'Ves':grapefruit.ves, 'Category':grapefruit.category, 'Price':grapefruit.price, 'Godnost':grapefruit.godnost, 'Volume':grapefruit.volume}, 
            {grapefruit.name:'Name', grapefruit.ves:'Ves', grapefruit.category:'Category', grapefruit.price:'Price', grapefruit.godnost:'Godnost', grapefruit.volume:'Volume'}]

tangerine_slov = [{'Name':tangerine.name, 'Ves':tangerine.ves, 'Category':tangerine.category, 'Price':tangerine.price, 'Godnost':tangerine.godnost, 'Volume':tangerine.volume}, 
            {tangerine.name:'Name', tangerine.ves:'Ves', tangerine.category:'Category', tangerine.price:'Price', tangerine.godnost:'Godnost', tangerine.volume:'Volume'}]

chicken_slov = [{'Name':chicken.name, 'Ves':chicken.ves, 'Category':chicken.category, 'Price':chicken.price, 'Godnost':chicken.godnost, 'Volume':chicken.volume}, 
            {chicken.name:'Name', chicken.ves:'Ves', chicken.category:'Category', chicken.price:'Price', chicken.godnost:'Godnost', chicken.volume:'Volume'}]

cheese_slov = [{'Name':cheese.name, 'Ves':cheese.ves, 'Category':cheese.category, 'Price':cheese.price, 'Godnost':cheese.godnost, 'Volume':cheese.volume}, 
            {cheese.name:'Name', cheese.ves:'Ves', cheese.category:'Category', cheese.price:'Price', cheese.godnost:'Godnost', cheese.volume:'Volume'}]

m = [milk_slov, chips_slov, butter_slov, lemon_slov, chipsy_fish_slov, creckers_slov, grapefruit_slov, tangerine_slov, chicken_slov, cheese_slov]

with open('C:/PAPKA_PLA_RABOTA/Py_2/tamplates/index.json', 'w', encoding='utf8') as outfile:
    json.dump(m, outfile, ensure_ascii=False, indent=2)


def json_s(request):
    pr1 = Producti('Milk', 1500, 'Dairy products', 67, 7, 1000)
    pr2 = Producti('Chips', 150, 'Snacks', 103, 100, 500)
    pr3 = Producti('Butter', 450, 'Dairy products', 327, 21, 200)
    pr4 = Producti('Lemon', 40, 'Сitrus_fruit', 17, 62, 32)
    pr5 = Producti('Crispy fish', 250, 'Snacks', 72, 120, 300)
    pr6 = Producti('Crackers', 500, 'Snacks', 149, 99, 600)
    pr7 = Producti('Grapefruit', 300, 'Сitrus fruit', 64, 15, 400)
    pr8 = Producti('Tangerine', 16, 'Citrus fruit', 12, 13, 23)
    pr9 = Producti('Chicken', 1600, 'Meat', 478, 4, 612)
    pr10 = Producti('Cheese', 300, 'Dairy products', 423, 13, 400)
    m = [pr1, pr2, pr3, pr4, pr5, pr6, pr7, pr8, pr9, pr10]
    return JsonResponse(m, safe=False, encoder=ProductEncoder_2)

Categor = {
    'milk':r'C:\PAPKA_PLA_RABOTA\Py_2\images\Dairy_products.jpeg',
    'chips':r'C:\PAPKA_PLA_RABOTA\Py_2\images\Snacks.jpeg',
    'butter':r'C:\PAPKA_PLA_RABOTA\Py_2\images\Dairy_products.jpeg',
    'lemon':r'C:\PAPKA_PLA_RABOTA\Py_2\images\Сitrus_fruit.jpeg',
    'meat':r'C:\PAPKA_PLA_RABOTA\Py_2\images\Meat.jpeg',
    'balloon':r"C:\PAPKA_PLA_RABOTA\Py_2\images\Air_balloon.jpeg"
}

def Citrus_fruit(request):
    file = Categor.setdefault('lemon')
    return FileResponse(open(file, 'rb'))

def Snacks(request):
    file = Categor.setdefault('chips')
    return FileResponse(open(file, 'rb'))

def Dairy_products(request):
    file = Categor.setdefault('milk')
    return FileResponse(open(file, 'rb'))

def Meat(request):
    file = Categor.setdefault('meat')
    return FileResponse(open(file, 'rb'))

def Air_balloon(request):
    file = Categor.setdefault('balloon')
    return FileResponse(open(file, 'rb'))

def jsoni(request: JsonResponse):
    with open('C:/PAPKA_PLA_RABOTA/Py_2/tamplates/index.json') as outfile:
        m = json.load(outfile)
        return JsonResponse(m, safe=False, encoder=ProductEncoder)

def categories_view(request, keys: str):
    if keys == 'dairy_products':
        file = Categor.setdefault('milk')
        return FileResponse(open(file, 'rb'), as_attachment=True, filename='Dairy_products.jpeg')
    if keys == 'snacks':
        file = Categor.setdefault('chips')
        return FileResponse(open(file, 'rb'), as_attachment=True, filename='Snacks.jpeg')
    if keys == 'citrus_fruit':
        file = Categor.setdefault('lemon')
        return FileResponse(open(file, 'rb'), as_attachment=True, filename='Сitrus_fruit.jpeg')
    if keys == 'meat':
        file = Categor.setdefault('meat')
        return FileResponse(open(file, 'rb'), as_attachment=True, filename='Meat.jpeg')
    if keys == 'balloon':
        file = Categor.setdefault('balloon')
        return FileResponse(open(file, 'rb'), as_attachment=True, filename='Air_balloon.jpeg')
    else:
        raise Http404

def fil_ke(request, ke:int):
    a = list(Product.objects.all())
    c = len(a)
    b = list(Category.objects.all())
    if ke > c - 1:
        raise Http404
    return render(request, r'C:\PAPKA_PLA_RABOTA\Py_2\tamplates\product.html', {'products':a[ke]} | {'category':b} | {'ke':ke})


def nach(request):
    return render(request, r'C:\PAPKA_PLA_RABOTA\Py_2\tamplates\1_stranicha.html')

def productsi(request):
    selected_category_id = request.GET.get('category') # получаем значение выбранной категории из URL-адреса
    categories = Category.objects.all()
    selected_category = None
    
    # фильтруем список категорий, чтобы получить только выбранную категорию
    if selected_category_id:
        selected_category = categories.filter(id=selected_category_id).first()
    
    context = {
        'categories': categories,
        'selected_category': selected_category
    }

    category_id = request.GET.get('category')
    if category_id:
        try:
            category = Category.objects.get(id=category_id)
            products = Product.objects.filter(category=category)
        except Category.DoesNotExist:
            raise Http404
    else:
        products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'products.html', {'products': products} | {'categories': categories} | context)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class PersonEncoder(DjangoJSONEncoder):
    def default(self, obji):
        if isinstance(obji, Person):
            return {'Name': obji.name, 'age': obji.age}
        return super().default(obji)

def thx(request):
    return render(request, r'C:\PAPKA_PLA_RABOTA\Py_2\tamplates\thx.html')

def add(request):
    if request.method == "POST":
        form = ClientPostForm(request.POST, request.FILES, request.EMAIL)
        if form.is_valid():
            try:
                form.save()
            except:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = ClientPostForm
        file = r'C:\PAPKA_PLA_RABOTA\Py_2\tamplates\buy.html'
        return render(request, file, {'form':form})

def add_product(request):
    if request.method == "POST":
        form = ProductPostForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                form.add_error(None, "Ошибка заполнения формы!")
    else:
        form = ProductPostForm()
    return render(request, 'add/add_product.html', {'form':form})

def add_category(request):
    if request.method == "POST":
        form = CategoryPostForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                form.add_error(None, "Ошибка заполнения формы!")
    else:
        form = CategoryPostForm
        return render(request, 'add/add_category.html', {'form':form})

def prochee(request):
    return render(request, 'prochee.html')

def custom_handler404(request, exception):
    return render(request, r'C:\PAPKA_PLA_RABOTA\Py_2\tamplates\404.html', status=404)