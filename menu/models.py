from django.db import models

COMBO_CHOICES = [
    ('Qəlyan setləri','Qəlyan setləri'),
    ('Çay setləri','Çay setləri'),
    ('Pivə setləri','Pivə setləri'),
]

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    icon = models.ImageField()
    ordering = models.PositiveSmallIntegerField(default=8)
    
    def __str__(self):
        return self.title



class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,related_name='menu',null=True,blank=True)
    price = models.CharField(max_length=300)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    icon = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.title
    
class Combo(models.Model):
    combo_type = models.CharField(max_length=300,choices=COMBO_CHOICES,null=True,blank=True)
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