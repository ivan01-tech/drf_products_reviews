from django.contrib import admin
from .models import Category, Comment, Company, ImageModel, Product, ProductSize, ProductsSite, User

admin.site.site_title = "Product Review Admin"
admin.site.site_header = "Product Review Admin"


admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(ProductsSite)
# admin.site.register(Product)
admin.site.register(ProductSize)
admin.site.register(ImageModel)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "content")
    list_filter = ("category",)
