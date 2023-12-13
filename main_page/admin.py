from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(Subcategories)
admin.site.register(Product)
admin.site.register(User)
admin.site.register(ProductReviews)
admin.site.register(ProductReviewComments)
admin.site.register(Seller)
admin.site.register(Basket)
admin.site.register(Address)