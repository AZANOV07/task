from django.contrib import admin
from .models import Product, Images


class ImagesInline(admin.TabularInline):
    model = Images
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ImagesInline,)
