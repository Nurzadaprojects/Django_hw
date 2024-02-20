
from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpResponse

from product.models import Product, Category, Review

# admin.site.register(Product)


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 0
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rate', 'created_at', 'updated_at')
    list_display_links = ('title', )
    list_editable = ('rate', )
    list_filter = ('created_at', 'rate')
    search_fields = ('title', )
    readonly_fields = ('created_at', 'updated_at', 'id')
    fields = ('title', 'rate', )
    inlines = [CategoryInline]

    # def get_readonly_fields(self, request, obj=None):
    #     pass
    #
    # def get_queryset(self, request):
    #     pass

    # def has_add_permission(self, request):
    #     pass



admin.site.register(Category)
admin.site.register(Review)
