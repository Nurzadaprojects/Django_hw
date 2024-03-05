from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.http import JsonResponse
from django.db.models import Q
from product.models import Product
from product.forms import ProductForm2, ReviewForm
from django.core.paginator import Paginator




def test_view(requests):
    return HttpResponse('Hello it is my project!')

def date_view(requests):
    current_date = datetime.now()
    return JsonResponse({'current_date': current_date})
def bye_view(requests):
    return HttpResponse('Good bye!')




def main_view(request):
    if request.method == 'GET':
        print(request.user)
        return render(request, 'components/index.html')

def product_list_view(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        page = request.GET.get('page', 1)



        products = Product.objects.all()

        if search:
            products = products.filter(
                Q(title__icontains=search) |
                Q(content__icontains=search)

            )

        'products = [product1, product2, product3, product4, product5, product6, \
                      product7, product8, product9, product10]'
        'limit = 3, page = 1'
        'max_pages = 10 / 3 = 3.3333 => 4'

        'formula:'
        'start = (page -1) * limit'
        'end = start + limit'


        'example:'
        'page = 1, limit = 3'
        'start = (1 - 1) * 3 = 0'
        'end = 0 + 3 = 3'

        'page = 2, limit = 3'
        'start = (2 - 1) * 3 = 3'
        'end = 3 + 3 = 6'

        'page = 4, limit = 3'
        'start = (4 - 1) * 3 = 9'
        'end = 9 + 3 = 12'

        limit = 10
        max_pages = products.count() // limit
        pages = [i for i in range(1, max_pages + 2)]
        if max_pages % 1 != 0:
            max_pages = int(max_pages) + 1

        pages = [i for i in range(1, max_pages + 2)]

        # if len(pages) > 10:
        #     pages = pages[:10] + [max_pages + 1]

        start = (int(page) - 1) * limit
        end = start + limit

        products = products[start:end]

        context = {
            'products': products,
            'pages': pages
            }

        return render(
            request=request,
            template_name='products/product_list.html',
            context={'products': products}
        )



def product_detail_view(request, pk):
    for product in products:
        for review in product.reviews.all():
            print(review.title)
        context = {'products': products}



        return render(
            request=request,
            template_name='products/product_list.html',
            context={'products': products}
            )


def product_detail_view(request, pk):
    if request.method == 'GET':
        try:
            products = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return render(
                request=request,
                template_name='errors/404.html'
            )
        form = ReviewForm()
        context = {'product': products}

        return render(
            request=request,
            template_name='products/product_detail.html',
            context=context
        )

def create_review_view(request, pk):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if not form.is_valid():
            return rebder(
                request=request,
                template_name='products/product_detail.html',
                context={'form': form}
            )

        review = form.save(commit=False)
        review.pk = pk
        review.save()

        return redirect(f'/products/{pk}/')



def create_product_view(request):
    if request.method == 'GET':
        form = ProductForm2()

        return render(
            request=request,
            template_name='products/create_product.html',
            context={"form": form}

        )
    elif request.method == 'POST':
        form = ProductForm2(request.POST, request.FILES)
        if not form.is_valid():
            return render(
                request=request,
                template_name='products/create_product.html',
                context={"form": form}
            )


        # Product.objects.create(**form.cleaned_data)
        form.save()
        return redirect('/products/')




    
