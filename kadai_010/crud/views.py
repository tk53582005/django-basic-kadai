from django.views.generic import TemplateView, ListView
from .models import Product
from django.views.generic.edit import CreateView
from .models import Product
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.views.generic import DetailView
from .models import Product

class TopView(TemplateView):
    template_name = "top.html"

class ProductListView(ListView):
    model = Product
    paginate_by = 3

class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'

class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('list')

class ProductDetailView(DetailView):
    model = Product
    template_name = 'crud/product_detail.html'
    context_object_name = 'product'