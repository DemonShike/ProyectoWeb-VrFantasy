from django.shortcuts import render, HttpResponse,redirect,get_object_or_404
from questweb.forms import FormArticle
from questapp.models import Article,Category
from django.contrib import messages

# Create your views here.

def index(request):

    return render(request, 'index.html')

def about_us(request):
    
    return render(request, 'about_us.html')


def products(request):
    articulos = Article.objects.filter(status = True).order_by('-created_at')
    #posible forma ,crear una var que recorra todas las categorias,pasarla como variable al render, y en el html recorrerla para que muestre todas las categorias en forma de link para filtrar en otra view
    return render(request, 'products.html',{
        'articulos': articulos
    })

def products_detailed(request, slug):
    articulos = Article.objects.get(slug=slug)

    return render(request, 'product_detailed.html',{
        'articulos': articulos
    })

def form(request): #Recibe los datos enviados de /formulario/
    if request.method == 'POST':

        formulario = FormArticle(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            name_products = data_form['name_products']
            shipping_type = data_form['shipping_type']
            shipping_price = data_form['shipping_price']
            description_products = data_form['description_products']
            product_city = data_form['product_city']
            product_price = data_form['product_price']
            status = data_form['status']

            articulo = Article(
                name_products = name_products,
                shipping_type =  shipping_type,
                shipping_price = shipping_price,
                description_products =  description_products,
                product_city = product_city,
                product_price = product_price,
                status = status
            )

            articulo.save()

            
            #return HttpResponse(articulo.name_products + ' ' + articulo.shipping_type + ' ' + articulo.shipping_price + ' ' + articulo.description_products + ' ' +  articulo.product_city)
            messages.success(request, f'Has creado correctamente el articulo {articulo.name_products}')
            return redirect('products')
    formulario = FormArticle()

    return render(request, 'formulario.html',{
        'form' : formulario
    })


def categories(request, category_name):

    category = get_object_or_404(Category ,name=category_name)
    articulo = Article.objects.filter(categories = category)

    return render(request, 'categories.html',{
        'category':category,
        'articulos':articulo
    })