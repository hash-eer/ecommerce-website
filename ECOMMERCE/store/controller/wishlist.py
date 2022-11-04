from django.shortcuts import render,redirect
from store.models import *
from django.contrib import messages
from django.http import JsonResponse

from store.models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='loginpage')
def index(request):
    wishlistitem=wishlist.objects.filter(user=request.user)
    context={'wishlistitem':wishlistitem}
    return render(request,'store/wishlist.html',context)

def addtowishlist(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            product_check=Product.objects.get(id=prod_id)
            if(product_check):
                if(wishlist.objects.filter(user=request.user,product_id=prod_id)):
                    return JsonResponse({'status':"product already in wishlist found"})
                else:
                    wishlist.objects.create(user=request.user,product_id=prod_id)
                    return JsonResponse({'status':"product added to wishlist successfully"})
            else:
                return JsonResponse({'status':"no such product found"})
            
        else:
            return JsonResponse({'status':"login to continue"})
        
    return redirect('home')

def deletewishlistitem(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            if(wishlist.objects.filter(user=request.user,product_id=prod_id)):
                wishlistitem=wishlist.objects.get(product_id=prod_id)
                wishlistitem.delete()
                return JsonResponse({'status':"product removed from wishlist"})
            else:
               
                return JsonResponse({'status':"product not found in wishlist"})
        else:
            return JsonResponse({'status':"Login to Continue"})
    return redirect('home')
    