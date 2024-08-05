from django.shortcuts import render
from menu.models import *
# Create your views here.
def home(request):
    categories = Category.objects.all()
    product = Product.objects.all()
    combo = Combo.objects.all()
    sportitems = SportItem.objects.all()
    combo_types = [x[0] for x in COMBO_CHOICES]
    context = {
        'combo':combo,
        'categories':categories,
        'product':product,
        'sportitems':sportitems,
        'combo_types':combo_types
    }
    return render(request,'index.html',context)