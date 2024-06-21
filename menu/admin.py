from django.contrib import admin
from menu.models import Category,Product,Combo,ComboItems,SportItem,SubCategory
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)

class ComboItemsInline(admin.TabularInline):  
    model = ComboItems
    extra = 0

class ComboAdmin(admin.ModelAdmin):
    inlines = [ComboItemsInline]
    
admin.site.register(Combo,ComboAdmin)
admin.site.register(SportItem)
admin.site.register(SubCategory)