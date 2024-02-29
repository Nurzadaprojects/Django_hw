from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.http import JsonResponse


from product.models import Product
from product.forms import ProductForm2, ReviewForm




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
        products = Product.objects.all()

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




    
