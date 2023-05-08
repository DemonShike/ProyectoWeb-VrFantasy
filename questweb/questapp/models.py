from django.db import models

# Create your models here.

class Article(models.Model):

    
    name_products = models.CharField(max_length=150)
    shipping_type = models.BooleanField()
    shipping_price = models.BooleanField()
    description_products = models.TextField()
    product_city = models.CharField(max_length=30)
    image_product = models.ImageField(default='null', upload_to='image_products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)

    class Meta: #Esta clase se utliza para cambiar los aspectos visuales de los modelos en el panel admin
        verbose_name = "Article"#cambiamos el nombre singular 
        verbose_name_plural = "Articles"

    def __str__(self):
        if self.status:
            status = "Publicado"
        else:
            status = "Privado"
        return f"{self.name_products} | Estado: {status} | Creado: {(self.created_at.strftime('%Y-%m-%d'))[:10]}"

"""
class image_secondary(models.Model):
    secondary_image = models.ImageField(default='null')
"""