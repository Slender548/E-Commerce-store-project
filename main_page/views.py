from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def show_main(request):
    products = Product.objects.all()
    return render(request, "main_page/main_page.html", {'products': products})

def show_product(request, product_id):
    product = Product.objects.get(id=product_id)
    avg_rating = product.average_rating()
    rating_count = product.ProductReviews.all().count()
    context = {
        'product': product, 
        "avg_rating": avg_rating,
        "rating_count": rating_count,
    }
    return render(request, "main_page/product.html", context)