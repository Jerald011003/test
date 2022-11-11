from django.shortcuts import render
from .models import Product

# Create your views here.
from django.views.generic import ListView, DetailView

#listview
class ProductListView(ListView):
    #queryset = Product.objects.all()
    template_name = "list.html"

    #Model Manager
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

#DetailView
class ProductDetailView(DetailView):
    #queryset = Product.objects.all()
    #print(queryset)
    template_name = "detail.html"

    # Model Manager
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk =self.kwargs.get('pk')
        return Product.objects.filter(pk=pk)

#featured

class ProductFeaturedListView(ListView):
    template_name = "list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()

class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "featured-detail.html"
#has STOPPED ON Lesson 7: Slug Field and Signals