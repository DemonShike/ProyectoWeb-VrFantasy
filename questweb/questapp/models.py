from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.





class Category(models.Model):
    name = models.CharField( max_length=100, verbose_name='Name')
    description = models.CharField(max_length=255, verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at: ')
        
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):

        return self.name


class Article(models.Model):

    
    name_products = models.CharField(max_length=150)
    shipping_type = models.BooleanField()
    shipping_price = models.BooleanField()
    description_products = RichTextField(verbose_name="Description")
    product_city = models.CharField(max_length=30)
    image_product = models.ImageField(default='null', upload_to='image_products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False, verbose_name='¿Public?')
    min_image_one =  models.ImageField(default='null', upload_to='image_products_min')
    min_image_two =  models.ImageField(default='null', upload_to='image_products_min')
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE, editable=False, null=True)
    categories = models.ManyToManyField(Category, verbose_name='Categories', blank=True)
    slug = models.CharField(unique=True, max_length=150, verbose_name="URL FRIENDLY :D",default='none')


    
    def save(self, *args, **kwargs):
        if  self.slug == "none":
            base_slug = slugify(self.name_products)
            slug = base_slug
            counter = 1
            while Article.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug

        super().save(*args, **kwargs)

    class Meta: #Esta clase se utliza para cambiar los aspectos visuales de los modelos en el panel admin
        verbose_name = "Article"#cambiamos el nombre singular 
        verbose_name_plural = "Articles"

    def __str__(self):
        if self.status:  
            status = "Publicado"
        else:
            status = "Privado"
        return f"{self.name_products} | Estado: {status} | Creado: {(self.created_at.strftime('%Y-%m-%d'))[:10]}"



class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE, editable=False, null=True,related_name='usercart') 
    articles = models.ManyToManyField(Article, through='CartItem')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    def final_total_price(self): #esta funcion toma como variable de forma inversa todos los campos de CartItem con los metodos/funciones.Luego itera ,en esta caso le hacemos iterar total_price,que es la funcion que multiplica cada relacion de articulos x cantidad,y los suma con el += a total price,asi 
        total_price = 0          # constantemente hasta que se iteran todas las relaciones de quantity*article teniendo en cuenta que solo los hace con las que tienen relacion al cart del user actual dado que es una relacion foreign key  y solo a un usuario le pueden pertenercer las relaciones iteradas
        cart_items = self.sexocart.all()
        for cart_item in cart_items:
            total_price += cart_item.total_price()
        return total_price 
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, verbose_name="cart",on_delete=models.CASCADE, related_name='sexocart')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Cart #{self.cart.pk} - Article: {self.article.name_products} - Quantity: {self.quantity} ah{self.cart.id}"
    
    def total_price(self):

        return self.quantity*self.article.product_price
    
