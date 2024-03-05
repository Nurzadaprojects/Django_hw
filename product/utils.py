from .models import Product





def create_100_products():
    products = []
    for i in range(100):
        product = Product(
            title=f'Title {i}',
            content=f'Content {i}',
        )
        products.append(product)

    Product.objects.bulk_create(products)
