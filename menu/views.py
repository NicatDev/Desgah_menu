from django.shortcuts import render
from menu.models import *
# Create your views here.
def home(request):
    categories = Category.objects.all()
    product = Product.objects.all()
    combo = Combo.objects.all()
    sportitems = SportItem.objects.all()
    context = {
        'combo':combo,
        'categories':categories,
        'product':product,
        'sportitems':sportitems
    }
    return render(request,'index.html',context)