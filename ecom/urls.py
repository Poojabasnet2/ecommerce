from django.urls import path
from . import views
from .views import ProductList,ProductDetail
from django.conf import settings
from ecom import views

from django.conf.urls.static import static
app_name='ecom'

urlpatterns = [
    
     path('', views.ProductList.as_view(), name='products'),
     path('price_list', views.ProductPriceList.as_view(), name='price_list'),
     path('category/<str:category_name>/', views.CategoryList.as_view(), name='category'),
     path('details/<int:pk>', views.ProductDetail.as_view(), name='ecom_details'),
     path('signup', views.SignupView.as_view(), name='signup'),
     path('change_password', views.MyPassWordChangeView.as_view(), name='password_change'),
     path('change_password/done', views.MyPassWordResetView.as_view(), name='password_change_done'),
     
     
     
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
     