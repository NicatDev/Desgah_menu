from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    icon = models.ImageField()

    def __str__(self):
        return self.title
    
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='menu')
    price = models.CharField(max_length=300)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    icon = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.title
    
class Combo(models.Model):
    title = models.CharField(max_length = 300)
    icon = models.ImageField()
    price = models.CharField(max_length=300)
    def __str__(self):
        return self.title

class ComboItems(models.Model):
    title = models.CharField(max_length=200)
    combo = models.ForeignKey(Combo,on_delete=models.CASCADE,related_name='comboitems')

    def __str__(self):
        return self.title
    
class SportItem(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title