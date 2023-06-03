from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.CategoryListView.as_view(), name="category_list"),
    path('<int:pk>/', views.CategoryProductView.as_view(), name="category_product"),
    path('ajax/search-and-filter/', views.load_search_and_filter, name="ajax_load_search_and_filter"),
    
]