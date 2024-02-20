from django.db import models



class Review(models.Model):
    title = models.CharField(max_length=50)


    def __str__(self):
        return self.title


class Product(models.Model):   
    image = models.ImageField(upload_to='product_images', null=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reviews = models.ManyToManyField(
        Review,
        related_name='products'
    )


    def __str__(self):
        return f'{self.title} - {self.rate}'

# class ProductInfo(models.Model):
#     product = models.OneToOneField(
#         Product,
#         on_delete=models.CASCADE,
#         related_name='info'
#     )
#     likes = models.IntegerField(default=0)
#     dislikes = models.IntegerField(default=0)
#     views = models.IntegerField(default=0)
#
#     def __str__(self):
#         return f'Info for {self.post.title}'

class Category(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='categories'
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment for {self.product.title}'
