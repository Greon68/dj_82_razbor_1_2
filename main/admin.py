from django.contrib import admin

from main.models import Category, Product, Order, OrderProduct
# from django.forms import  BaseInlineFormSet
from django import forms

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','category']
    list_filter = ['category']
    search_fields = ['name']



class ProductFormSet(forms.BaseInlineFormSet):
    ''' FormSet . Проверка на правильность введённого значения'''
    def clean(self):
        for form in self.forms:
            quantity = form.cleaned_data['quantity']
            if quantity < 0 :
                raise forms.ValidationError('Ошибка ввода количества товара ( параметр QUANTITY )')
        return super().clean()



class OrderProductInline(admin.TabularInline):
    ''' Inline - модель'''
    model =  OrderProduct
    # fields = ['product','quantity',]
    formset = ProductFormSet
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    inlines = [ OrderProductInline ]


admin.site.register(Order,OrderAdmin)
admin.site.register(OrderProduct)