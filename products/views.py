from django.shortcuts import render

# Create your views here.
def all_products(request):
    products = Products.objects.all()
    return render(request, "products.html", {"products": products})
