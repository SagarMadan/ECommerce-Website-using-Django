from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
  name=models.CharField(max_length=20)
  def __str__(self):
    return self.name
  
class Product(models.Model):
  name=models.CharField(max_length=100)
  description=models.TextField()
  category=models.ForeignKey(Category,on_delete=models.CASCADE)
  price=models.DecimalField(max_digits=10,decimal_places=2)
  image=models.ImageField(upload_to='products/')
  discount=models.DecimalField(max_digits=10,decimal_places=2,null=True)
  def __str__(self):
    return self.name



class CartItem(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  product=models.ForeignKey(Product,on_delete=models.CASCADE)
  quantity=models.PositiveIntegerField(default=1)

  def __str__(self):
    return f"{self.product.name} - {self.user.username}"
  def total_price(self):
    return self.product.price*self.quantity