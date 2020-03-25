from django.urls import path

from api.views import product_list, product_detail, category_list,category_detail, product_by_category

urlpatterns = [
    path('products/', product_list),
    path('products/<int:id>/', product_detail),
    path('category/', category_list),
    path('category/<int:id>/', category_detail),
    path('categorypro/<int:id>/', product_by_category)

]