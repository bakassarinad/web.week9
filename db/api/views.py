from django.http.response import JsonResponse
from api.models import Product, Category
# Create your views here.
from django.http import Http404
def product_list(request):
    products = Product.objects.all()
    json_products = [p.to_json() for p in products]
    return JsonResponse(json_products, safe=False)
def product_detail(request, id):
    try:
        product = Product.objects.get(id = id)
        return JsonResponse(product.to_json())
    except Product.DoesNotExist as e:
        return JsonResponse({'error': 'there is no product'})
def category_list(request):
    categories = Category.objects.all()
    json_categories = [c.to_json() for c in categories]
    return JsonResponse(json_categories, safe=False)
def category_detail(request, id):
    try:
        category = Category.objects.get(id = id)
        return JsonResponse(category.to_json())
    except Category.DoesNotExist as e:
        return JsonResponse({'error': 'there is no category'})
def product_by_category(request, id):
    try:
        products = Product.objects.filter(category = id)
        json_products_by_category = [p.to_json() for p in products]
        return JsonResponse(json_products_by_category, safe = False)
    except:
        return JsonResponse({'error': 'No products in category'})
