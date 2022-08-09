from django.urls import path
from app import views
from app.views import MyObtainTokenPairView, RegisterView, ItemsView, ItemsListView, order_view, OrdersListView, \
      CartView, LogoutView, LogoutAllView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
      #items
      path('items/',ItemsView.as_view(),name='items'),
      path('items/<int:pk>/',ItemsListView.as_view(),name='itemslist'),
      #orders
      path('orders/',order_view.as_view(),name='order'),
      path('orders/<int:pk>/',OrdersListView.as_view(),name='orderslist'),
      #login
      path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
      path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
      #register
      path('register/', RegisterView.as_view(), name='auth_register'),
      path('<int:pk>/', views.Ratingview.as_view()),
      #logout
      path('logout/', LogoutView.as_view(), name='auth_logout'),
      path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
      #cart optional
      path('cart/',CartView.as_view(),name='cart')

]