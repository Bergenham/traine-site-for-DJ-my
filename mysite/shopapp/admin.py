from csv import DictReader
from django.urls import path
from django.contrib import admin
from django.shortcuts import render, redirect
from .models import Product, Order
from .admin_mixins import ExportAsCSVMixin
from .forms import CSVImportForm
from io import TextIOWrapper

@admin.action(description='Arhive all actions taken by the')
def fast_arhive(modeladmin, request, queryset):
    queryset.update(arvay=True)


@admin.action(description='Unarhive all actions taken by the')
def fast_unarhive(modeladmin, request, queryset):
    queryset.update(arvay=False)


class OrderInline(admin.TabularInline):
    model = Product.orders.through


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    change_list_template = 'shopapp/products_chage.html'
    actions = [fast_arhive, fast_unarhive, 'export_as_csv', ]
    inlines = [OrderInline, ]
    list_display = ('pk', 'name', 'description_s', 'prise', 'discount', 'arvay')
    list_display_links = 'pk', 'name',
    search_fields = ('name', 'description', 'prise')
    fieldsets = [
        (None, {'fields': ('name', 'description',)}),
        ('Price Information', {'fields': ('prise', 'discount'),
                               'classes': ('collapse',)})
    ]

    def description_s(self, obj: Product) -> str:
        if len(obj.description) < 50:
            return obj.description
        else:
            return obj.description[:50] + '...'

    def importSCV(self, request):
        if request.method == 'GET':
            form = CSVImportForm()
            context = {
                'form': form,
            }
            return render(request, 'admin/csv_form.html', context=context)
        form = CSVImportForm(request.POST, request.FILES)
        if not form.is_valid():
            context = {
                'form': form,
            }
            return render(request, 'admin/csv_form.html', context=context, status=400)

        csv_file = TextIOWrapper(
            form.files['csv_file'].file,
            encoding=request.encoding,
        )
        reader = DictReader(csv_file)

        products = [
            Product(**row)
            for row in reader
        ]
        Product.objects.bulk_create(products)
        self.message_user(request, "Data seccses")
        return redirect("..") #Вернуться на одну страницу выше

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path('import-csv/', self.importSCV, name='import_pr_CSV')
        ]
        return new_urls + urls


class ProductInline(admin.TabularInline):
    model = Order.products.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = 'delivery_adres', 'promocod', 'created_at', 'user_verbose',
    list_display_links = 'delivery_adres', 'user_verbose'

    inlines = [ProductInline, ]

    def get_queryset(self, request):
        return Order.objects.select_related('user').prefetch_related('products')

    def user_verbose(self, obj: Order) -> str:
        return obj.user.first_name or obj.user.username
