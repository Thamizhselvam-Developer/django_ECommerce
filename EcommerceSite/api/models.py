from django.db import models
class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    description= models.CharField(max_length=100,blank=True, null=True)
    def __str__(self):
        return self.categoryName
class Products(models.Model):
    productName=models.CharField(max_length=100)
    productImageLink=models.ImageField(upload_to="./Uploads" ,blank=True,null=True)
    productPrice=models.DecimalField(max_digits=10,decimal_places=2)
    
    category=models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
            null=True,
        blank=True
    )
    def __str__(self):
        return self.productName
    
