from django.shortcuts import render, HttpResponse,redirect,get_object_or_404
from questweb.forms import FormArticle
from questapp.models import Article,Category, Cart, CartItem
from django.contrib import messages
from django.core.paginator import Paginator #importando paginator
from django.contrib.auth.forms import UserCreationForm # importing the object 
from questweb.forms import RegisterForm #importando el modelo definitivo para el registro
from django.contrib.auth import authenticate, login, logout #metodos para login
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User

# Create your views here.

def index(request):

    return render(request, 'index.html')

def about_us(request):
    
    return render(request, 'about_us.html',{
        'title':"About us | Vr Fantasy"
    })


def products(request):
    #recoger busqueda
    search = request.GET.get('search')
    if search:
        articulos = Article.objects.filter(name_products__contains = search,status = True).order_by('-created_at')
    else:
        articulos = Article.objects.filter(status = True).order_by('-created_at')

        
    paginator = Paginator(articulos, 8)

    #recoger numero pagina
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)




    return render(request, 'products.html',{
        'articulos': page_articles
    })

def products_detailed(request, slug):
    articulos = Article.objects.get(slug=slug)

    return render(request, 'product_detailed.html',{
        'articulos': articulos
    })

@staff_member_required
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

    search = request.GET.get('search')
    if search:
        articulo = Article.objects.filter(categories = category, name_products__contains = search)
    else:
        articulo = Article.objects.filter(categories = category)

    paginator = Paginator(articulo, 1)

    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request, 'categories.html',{
        'category':category,
        'articulos':page_articles
    })


def register_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        register_form = RegisterForm()

        if request.method == 'POST':
            register_form= RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()

                messages.success(request, 'You have successfully Registered')

                return redirect('register')

        return  render(request, 'register.html',{
            'register_form' : register_form,
            'title': 'Register | Vr Fantasy',
            'title_form':'Register'
        })

def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            remember_me = request.POST.get('remember_me')

            user = authenticate(request, username=username, password=password)

            if user is not None and user.check_password(password):#check password sirve poara comprobar si la contraseña conincide en la que hay en la base de datos ,quise hacer 2 if para que me dijera un mensajer de error o contraseña incorrecta dependiendo pero no sirvio,aun asi la deje junto a la de auth por que me parece un buen recurso
                login(request, user)

                if remember_me:# if de remember me para el recuerdame
                        request.session.set_expiry(settings.SESSION_COOKIE_AGE)  # 2 weeks
                    
                else:
                        request.session.set_expiry(0)
                        
                messages.success(request, f'Welcome {username}')
                return redirect('index')
                    
            else:
                messages.error(request, 'Wrong Password or Username')


        return render(request, 'login.html',{
            'title_form':'Login'
            
            
        })


def error_404(request, exception):

    return render(request, 'error404.html', status=404)

def end_page(request):

    return render(request, 'end_page.html')


def logout_user(request):#log out

    logout(request)

    return redirect ('index')

@login_required(login_url="login")
def view_cart(request):
    user = request.user

       # Verificar si el usuario ya tiene un carrito
    try:
        cart = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        # Si el carrito no existe, crear uno nuevo
        cart = Cart.objects.create(user=user)

    return render(request, 'cart.html', {'cart':cart})

@login_required(login_url="login")
def add_to_cart(request, id):
    user = request.user

    
    article = Article.objects.get(id=id)
    cart = Cart.objects.get(user=user)

    if article in cart.articles.all():
    # El artículo ya está en el carrito, actualizar la cantidad
        cart_item = CartItem.objects.get(cart=cart, article=article)
        cart_item.quantity += 1
        cart_item.save()
    else:
        # Agregar el artículo al carrito con cantidad 1
        CartItem.objects.create(cart=cart, article=article, quantity=1)

    return redirect('view_cart')


#funcion borra articulo del carro por la id que crea el cart items NO EL DEL ARTICULO ORIGINAL ,SINO LA CREADA DE LA RELACION
@login_required(login_url="login")
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')

@login_required(login_url="login")
def remove_one_to_cart(request, id):
    user = request.user

    
    article = Article.objects.get(id=id)
    cart = Cart.objects.get(user=user)

    if article in cart.articles.all():
    # El artículo ya está en el carrito, eliminar 1
        cart_item = CartItem.objects.get(cart=cart, article=article)
        cart_item.quantity -= 1
        cart_item.save()


    return redirect('view_cart')

def privacy_policy(request):

    return render(request, "privacy_policy.html",{
        'title':"Other | VrFantasy"
    })

@login_required(login_url="login")
def about_me(request):
    user= request.user

    try:
        cart = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        # Si el carrito no existe, crear uno nuevo
        cart = Cart.objects.create(user=user)
        
    return render(request, 'about_me.html',{'cart':cart})

def so_far(request):

    return render(request, 'error404.html')