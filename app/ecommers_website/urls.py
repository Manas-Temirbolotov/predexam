"""ecommers_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from account.views import ProfileRegisterView
from shop import views as shop_views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


account_router = DefaultRouter()
account_router.register('register', ProfileRegisterView)

shop_router = DefaultRouter()
shop_router.register('category', shop_views.CategoryViewSet)


schema_view = get_schema_view(
   openapi.Info(
      title="Ecommerce API",
      default_version='v0.1',
      description="API для интернет магазина",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth', include('rest_framework.urls')),
    path('api/auth/token', obtain_auth_token),
    path('api/account/', include(account_router.urls)),
    path('api/shop/', include(shop_router.urls)),

    path('api/shop/category/<int:category_id>/item/', shop_views.ItemListCreateAPIView.as_view()),
    path('api/shop/category/<int:category_id>/item/<int:pk>/', shop_views.ItemListCreateAPIView.as_view()),
    path('api/shop/category/<int:category_id>/item/<int:item_id>/order/', shop_views.OrderListCreateAPIView.as_view()),
    path('api/shop/category/<int:category_id>/item/<int:item_id>/order/<int:pk>/',
         shop_views.OrderRetrieveUpdateDestroyAPIView.as_view()),

    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc_ui'),
    path('json_doc/', schema_view.without_ui(cache_timeout=0), name='json_doc'),

]
