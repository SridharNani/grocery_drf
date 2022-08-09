# Create your views here.
from rest_framework.views import APIView
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken

from .serializer import MyTokenObtainPairSerializer, ProdcutSerializer, FeedbackSerializer, OrderSerializer, \
    CartSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import *
from django.contrib.auth.models import User
from .serializer import RegisterSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ItemsView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    # permission_classes=(AllowAny)
    serializer_class=ProdcutSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = ProdcutSerializer(queryset, many=True)
        return Response(serializer.data)

class ItemsListView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class=ProdcutSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

class Ratingview(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class=FeedbackSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

class order_view(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    # permission_classes=(AllowAny)
    serializer_class = OrderSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

class OrdersListView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class=OrderSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

class CartView(generics.CreateAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]
    pagination_class = None
    queryset = OrderItem.objects.all()
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        new_order_item = serializer.save()
        user = User.objects.filter(id=self.request.user.id).first()
        new_order = OrderItem.objects.create(user=user)
        new_order.items.add(new_order_item)

        def __str__(self):
            return self.user

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class LogoutAllView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)