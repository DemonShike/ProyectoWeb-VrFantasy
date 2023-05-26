from .models import Category, Article

def get_categories(request):
    
    ids= Article.objects.filter(status=True).values_list('categories', flat=True)
    categories = Category.objects.filter(id__in=ids).values_list('name', 'description')
    
    return {
        'categories':categories,
        'ids':ids
    }