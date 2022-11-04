from email import message
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'store/index.html')

def collections(request):
    category=Category.objects.filter(status=0)
    context= {
        'category':category
    }
    return render(request,'store/collections.html',context)

def collectionsview(request,slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products=Product.objects.filter(category__slug=slug)
        category=Category.objects.filter(slug=slug).first()
        context={
            'products':products,
            'category':category
        }
        return render(request,'store/products/index.html',context)
    else:
        messages.warning(request,"link followed was broken and no category found")
        return redirect('collections')
    
def productview(request,cate_slug,prod_slug):
    if(Category.objects.filter(slug=cate_slug,status=0)):
        if(Product.objects.filter(slug=prod_slug,status=0)):
            products=Product.objects.filter(slug=prod_slug,status=0).first()
            print(products.quantity)
            context={'products':products}
        else:
            message.error(request,"no such product found")
            return redirect('collections')
    else:
        message.error(request,"no such category found")
        return redirect('collections')
    return render(request,'store/products/view.html',context)

from django.http import JsonResponse
def productlistajax(request):
    products=Product.objects.filter(status=0).values_list('name',flat=True)
    productlist=list(products)
    return JsonResponse(productlist,safe=False)

def searchproduct(request):
    if request.method=="POST":
        searchedterm=request.POST.get('productsearch')
        if searchedterm == "":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            product=Product.objects.filter(name__contains=searchedterm).first()
            
            if product:
                return redirect('collections/'+product.category.slug+'/'+product.slug)
            else:
                messages.info(request,"No product matched the Search")
                return redirect(request.META.get('HTTP_REFERER'))
            
    return redirect(request.META.get('HTTP_REFERER'))