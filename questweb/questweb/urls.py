"""questweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from questapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('about-us/', views.about_us, name='about_us'),
    path('formulario/', views.form, name='form'),
    path('formulario/<str:slug>', views.products_detailed, name='products_detailed'),
    path('categories/<str:category_name>', views.categories, name='categories'),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name="login"),
    path('error404/', views.error_404, name="error404"),
    path('logout/', views.logout_user, name='logout'),
    path('cart/',views.view_cart, name="view_cart"),
    path('add-to-cart/<int:id>', views.add_to_cart, name="add_to_cart"),
    path('cart-delete/<int:item_id>', views.remove_from_cart, name="cart_delete"),
    path('remove-one-to-cart/<int:id>', views.remove_one_to_cart, name="remove_one"),
    path('end-page/', views.end_page, name="endpage"),
    path('other-more/', views.privacy_policy, name="other"),
    path('about-me/', views.about_me, name="about_me"),
    path('so-far', views.so_far, name="so-far")

    
]

# load images
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.error_404