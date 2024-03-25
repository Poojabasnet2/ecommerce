from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Product,Category
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
#Create your views here.
class ProductList(ListView):
    
    model=Product
    context_object_name="ecom"
    template_name='ecom/products.html'


    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(name__icontains=q)
        return queryset


    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     q = self.request.GET.get('q')
    #     if q:
    #         queryset = queryset.filter(name__icontains=q)
    #     return queryset

    # def get_queryset(self):
    #   return Employee.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['ecom'] = Product.objects.all()  # Fetch all categories
    #     return context

class ProductDetail(DetailView):
    model=Product
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['ecom'] = Product.objects.all()  # Fetch all categories
    #     return context
    template_name='ecom/details.html'
    success_url=reverse_lazy('ecom:products')

# class CategoryList(ListView):
#     model = Product
#     template_name = 'ecom/category.html'
    
#     queryset = Product.custom_objects.filter(price__gte=500)
    
# class ProductPriceList(ListView):
#     model = Product
#     template_name = 'ecom/price_list.html'
#     queryset = Product.custom_objects.all().filter(price__gte=800)


class ProductPriceList(ListView):
    model = Product
    template_name='ecom/price_list.html'
    queryset=Product.custom_objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ecom"] = self.queryset
        return context
    def get_queryset(self):
        return super().get_queryset()


class CategoryList(ListView):
    model = Product
    template_name='ecom/category.html'
    context_object_name = 'ecom'

    # def get_queryset(self):
    #     return self.model.custom_objects.filter(name__icontains=self.request.GET.get(q))

    

    
    
    
    def get_queryset(self):
        category_name = self.kwargs['category_name']  
        queryset=Product.custom_objects.filter(category__name=category_name)

        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(name__icontains=q)
        
        return queryset


class SignupView(CreateView):
    form_class=UserCreationForm
    template_name="registration/signup.html"
    success_url=reverse_lazy("login")

class MyPassWordChangeView(PasswordChangeView):
    template_name="registration/password_change.html"
    success_url=reverse_lazy("login")

class MyPassWordResetView(PasswordResetDoneView):
    template_name="registration/password_reset.html"
    success_url=reverse_lazy("login")

