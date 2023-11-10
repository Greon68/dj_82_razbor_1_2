from django.shortcuts import render, get_object_or_404

from main.models import Product


def products_list(request):
    products= Product.objects.all()
    template_name = 'main/list.html'
    # print(request.GET)
    sort = request.GET.get('sort','')
    if sort:
        products = products.order_by(sort)
    search = request.GET.get('search','')
    if search:
        products = products.filter(name__icontains=search)

    return render(request, template_name,context={'products':products} )

def product_details(request,product_id):
    product= get_object_or_404( Product, id= product_id)
    template_name='main/details.html'
    return render(request, template_name, context={'product': product})