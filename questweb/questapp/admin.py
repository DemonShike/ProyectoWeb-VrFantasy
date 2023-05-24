from django.contrib import admin
from .models import Article, Category

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)


class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','user','updated_at')

    def save_model(self, request, obj, form, change): #esta funcion asigna al objeto creado,como usuario que lo creo,el que lo este creando en el admin panel
        if not obj.user_id:
            obj.user_id = request.user.id

        obj.save()



# Register your models here.

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)


#Names AdminPanel
admin.site.site_header = "Vr Fantasy Administration"
admin.site.site_title = "Vr Fantasy" 
admin.site.index_title = "Administration"

