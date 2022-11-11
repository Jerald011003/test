from django.shortcuts import render
from products.models import Product

# Create your views here.
from django.views.generic import ListView

#Search
class SearchProductView(ListView):
    #queryset = Product.objects.all()
    template_name = "search.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    #Model Manager
    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.filter(title__icontains='hat')
        return Product.objects.featured()


# Create your views here.
