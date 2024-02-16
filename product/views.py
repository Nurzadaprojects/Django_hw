from django.shortcuts import render
from django.http import HttpResponse


from product.models import Product




def test_view(requests):
    return HttpResponse('Hello it is my project!')


def main_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')

def product_list_view(request):
    if request.method == 'GET':
        products = Product.objects.all()


        return render(
            request=request,
            template_name='products/product_list.html',
            context={'products': products}

            )

