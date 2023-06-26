from django.contrib import admin
from .models import Article, Category, Cart, CartItem

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    search_fields = ('name',)


class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','user','updated_at', 'pk')
    search_fields = ('name_products','description_products',)
    list_filter = ('product_city','status','categories','user__username')
    list_display = ('name_products','status','created_at')
    ordering = ('created_at',)

    def save_model(self, request, obj, form, change): #esta funcion asigna al objeto creado,como usuario que lo creo,el que lo este creando en el admin panel
        if not obj.user_id:
            obj.user_id = request.user.id

        obj.save()



# Register your models here.

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Cart)
admin.site.register(CartItem)

#Names AdminPanel
admin.site.site_header = "Vr Fantasy Administration"
admin.site.site_title = "Vr Fantasy" 
admin.site.index_title = "Administration"

