from django.contrib import admin
from .models import Article
# Register your models here.

admin.site.register(Article)

#Names AdminPanel
admin.site.site_header = "Vr Fantasy Administration"
admin.site.site_title = "Vr Fantasy" 
admin.site.index_title = "Administration"
