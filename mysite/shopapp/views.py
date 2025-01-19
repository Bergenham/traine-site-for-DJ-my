import logging
from csv import DictWriter
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group
from timeit import default_timer

from django.views.decorators.cache import cache_page
from rest_framework.parsers import MultiPartParser
from rest_framework.filters import SearchFilter, OrderingFilter
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.request import Request
from rest_framework.response import Response
from django.core.cache import cache
from .com import csv_product
from .models import Product, Order
from .forms import ProductForm, Group_form
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action, parser_classes
from .serializers import ProductSerializers
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator

log = logging.getLogger(__name__)

class ShopIndexView(View):

    def get(self, request: HttpRequest):
        product = [
            ('Laptop', 1488),
            ('Desktop', 1200),
            ('Smartphone', 999)
        ]

        context = {
            'timer': default_timer(),
            'product': product,
        }

        log.debug('product: s%', product)
        log.info('rendering shop index')
        return render(request, 'shopapp/shopapp_index.html', context=context)


class Group_index_View(View):
    def get(self, request: HttpRequest):
        context = {
            'groups': Group.objects.prefetch_related('permissions').all(),
            'form': Group_form(),
        }
        return render(request, 'shopapp/huiny.html', context=context)

    def post(self, request):
        form = Group_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect(request.path)



class Product_list_View(ListView):
    template_name = 'shopapp/product_list.html'
    # model = Product
    context_object_name = 'products'
    queryset = (Product.objects.filter(arvay=False))


class Order_list(LoginRequiredMixin, ListView):
    queryset = (Order.objects
                .select_related('user')
                .prefetch_related('products')
                )
    context_object_name = 'order'


class Product_Create_View(CreateView):
    model = Product
    fields = 'name', 'prise', 'description', 'discount'
    success_url = reverse_lazy("shopapp:product_list")


class Product_Update_View(UpdateView):
    model = Product
    fields = 'name', 'prise', 'description', 'discount'
    template_name_suffix = '_update'

    def get_success_url(self):
        return redirect(
            "shopapp:product_update",
            kwargs={"pk": self.object.pk}
        )


class Product_Delete_View(DeleteView):
    model = Product
    success_url = reverse_lazy("shopapp:product_list")

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.arvay = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class Product_Detals_Views(DetailView):
    template_name = 'shopapp/product_detals.html'
    model = Product
    context_object_name = 'product'


class Order_Details_View(PermissionRequiredMixin, DetailView):
    permission_required = "shopapp.view_order"
    queryset = (Order.objects
                .select_related('user')
                .prefetch_related('products')
                )
    context_object_name = 'order'

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]
    search_fields = ['name', 'description']

    filterset_fields = [
        'name',
        'description',
        'prise',
        'arvay',
    ]

    ordering_fields = [
        'pk',
        'name',
        'prise',
    ]

    @method_decorator(cache_page(timeout=20)) #time
    def list(self, *args, **kwargs):
        return super().list(self, *args, **kwargs)

    @action(methods=['get'], detail=False)#флаг false указывает на то, что путь к d_csv построин на основе адреса для списка
    def download_csv(self, request: Request):
        response = HttpResponse(content_type='text/csv')
        filename = 'product-export.csv'
        response['Content-Disposition'] = f'... {filename}'
        queryset = self.filter_queryset(self.get_queryset())
        fields = [
        'name',
        'description',
        'prise',
        'discount',
        ]
        queryset = queryset.only(*fields)
        writer = DictWriter(response, fieldnames=fields)
        writer.writeheader()

        for product in queryset:
            writer.writerow({
                i: getattr(product, i)
                for i in fields
            })
        return response

    @action(methods=['post'], detail=False, parser_classes=[MultiPartParser],)
    def upload_csv(self, request: Request):
        products = csv_product(
            request.FILES["file"].file,
            encoding=request.encoding,
        )
        ser = self.get_serializer(products, many=True)
        return Response({ser.data})

class ProductsDataExportView(View):
    def get(self, request: HttpRequest):
        _key = "pd_cache"
        pd = cache.get(_key)
        if pd is None:
            products = Product.objects.order_by('pk').all()
            products_data = [
                {
                    "pk": product.pk,
                    "name": product.name,
                    "price": product.prise,
                    "archived": product.arvay,
                }
                for product in products
            ]
            cache.set(_key, products_data, 200)
        return JsonResponse({"products": products_data})

