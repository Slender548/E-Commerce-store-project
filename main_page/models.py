from django.db import models
from django.db.models import Avg
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
import datetime

# Create your models here.

class User(models.Model):
    photo = models.ImageField(upload_to='Users', blank=True, null=True)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=20, null=True, blank=True, validators=[RegexValidator(regex=r'^\d{9,15}$', message="Enter a valid phone number")])
    date_of_birth = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    street = models.CharField(max_length=30, blank=True, null=True)
    house = models.CharField(max_length=30, blank=True, null=True)
    apartment = models.CharField(max_length=30, blank=True, null=True)
    registered_on = models.DateField(auto_now_add=True)
    def show_address(self):
        return f"{self.country}, {self.city}, {self.street}, {self.house}{f', {self.apartment}' if self.apartment else ''}"
    def __str__(self):
        return self.username

class Product(models.Model):
    seller = models.ForeignKey('Seller', on_delete=models.CASCADE, related_name="Products", default=None)
    photo = models.ImageField(upload_to='Products')
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(1)])
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="Products")
    available_quantity = models.IntegerField(default=0)
    added_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    def average_rating(self):
        # Calculate the average rating using Django's aggregation functions
        average = self.ProductReviews.aggregate(Avg('stars'))['stars__avg']
        return average or 0  # Return 0 if there are no reviews yet

class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Basket")
    products = models.ManyToManyField(Product)
    sum = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.sum

class Subcategories(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="Subcategories", default=None)
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name


class ProductReviews(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="ProductReviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ProductReviews")
    stars = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(1)])
    photos = models.ImageField(upload_to='ProductReviews', blank=True, null=True)
    likes = models.IntegerField(default=0)
    review = models.TextField()

class ProductReviewComments(models.Model):
    review = models.ForeignKey(ProductReviews, on_delete=models.CASCADE, related_name="Comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    likes = models.IntegerField(default=0)

class Seller(models.Model):
    name = models.CharField(max_length=30)
    addresses = models.ManyToManyField('Address', related_name="SellerAddresses")
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    reviews = models.ManyToManyField(ProductReviews, related_name='Seller', null=True, blank=True)
    date_of_birth = models.DateField()
    def __str__(self):
        return self.name

class Address(models.Model):
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    house = models.CharField(max_length=30)