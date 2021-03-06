from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from store.api_views import ProductList, ProductCreate, RetrieveUpdateDestroyProduct
import store.views

urlpatterns = [
    path('api/v1/products/', ProductList.as_view()),
    path('api/v1/products/create', ProductCreate.as_view()),
    path('api/v1/products/<int:id>/reupde',
         RetrieveUpdateDestroyProduct.as_view()),

    path('admin/', admin.site.urls),
    path('products/<int:id>/', store.views.show, name='show-product'),
    path('cart/', store.views.cart, name='shopping-cart'),
    path('', store.views.index, name='list-products'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
