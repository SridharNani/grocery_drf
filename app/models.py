from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200 , blank=True)
    def __str__(self):
        return self.category_name

class QuantityVariant(models.Model):
    variant_name = models.CharField(max_length=100)

    def __str__(self):
        return self.variant_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description =models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="images", default="")
    quantity_type = models.ForeignKey(QuantityVariant, blank=True, null=True, on_delete=models.PROTECT)


    def __str__(self):
        return self.name


class Feedback(models.Model):
    SCORE_CHOICES = zip(range(6), range(6) )
    # user = models.CharField(max_length=50, null= True, default='anonymous user')
    item = models.ForeignKey(Product, on_delete=models.SET_NULL, null= True)
    rating = models.PositiveSmallIntegerField(choices=SCORE_CHOICES, blank=False)
    content = models.TextField(null=True,blank=True)

    def __str__(self):
        return 'Rating(Item ='+ str(self.item)+', Stars ='+ str(self.rating)+')'


class Order(models.Model):
    # id=models.ForeignKey(Product, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateField(auto_now_add=False, blank=True, null=True)
    ordered = models.BooleanField(default=False)



class OrderItem(models.Model):
    items = models.ManyToManyField(Product)
    product_quantity = models.PositiveIntegerField()