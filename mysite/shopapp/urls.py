from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (ShopIndexView,
                    Group_index_View,
                    Product_Detals_Views,
                    Product_list_View,
                    Order_Details_View,
                    Order_list,
                    Product_Create_View,
                    Product_Update_View,
                    Product_Delete_View,
                    ProductViewSet,
                    ProductsDataExportView
                    )

app_name = 'shopapp'

routers = DefaultRouter()
routers.register('products', ProductViewSet)

urlpatterns = [
    path('', ShopIndexView.as_view(), name='shop_index'),
    path('api/', include(routers.urls)),
    path('group/', Group_index_View.as_view(), name='groups_index'),
    path('product/', Product_list_View.as_view(), name='product_list'),
    path('product/<int:pk>/', Product_Detals_Views.as_view(), name='product_details'),
    path('product/create/', Product_Create_View.as_view(), name='product_input'),
    path('product/<int:pk>/update/', Product_Update_View.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', Product_Delete_View.as_view(), name='product_delete'),
    path('orders/', Order_list.as_view(), name="order_list"),
    path('order/<int:pk>/', Order_Details_View.as_view(), name='order_details'),
    path('products/export/', ProductsDataExportView.as_view(), name='p_ex'),
]
