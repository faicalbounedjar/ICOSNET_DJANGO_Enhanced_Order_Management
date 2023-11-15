from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('orders/',views.getAll,name='orders'),
    path('orders/<int:pk>/',views.getOrderById,name='get_Orders_By_Id'),
    path('new/',views.new_order,name='add_order'),
    path('orders/<int:pk>/update/', views.update_order, name='update_order'),
    path('orders/<int:pk>/delete/', views.delete_Order, name='delete_Order'),
    path('search/', views.getOrderByTitle, name='get_Order_By_Title'),
    path('search/<str:pk>', views.getOrderByTitleQuery, name='get_Order_By_Title_Query'),
]
