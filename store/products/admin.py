from django.contrib import admin
from products.models import ProductCategory, Product, Basket

# Register your models here

admin.site.register(ProductCategory)

admin.site.register(Basket)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description', 'short_description', ('price', 'quantity'), 'category')
    # readonly_fields = ('')
    ordering = ('name',)
    search_fields = ('name',)

class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product','quantity','created_timestamp')
    readonly_fields = ('product','quantity','created_timestamp',)
    extra = 0
