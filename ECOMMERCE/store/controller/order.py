from django.shortcuts import render,redirect
from store.models import *
from django.contrib import messages
from django.http import JsonResponse

from store.models import *
from django.contrib.auth.decorators import login_required

def index(request):
    orders=Order.objects.filter(user=request.user)
    context={'orders':orders}
    return render(request,'store/orders/index.html',context)

def vieworder(request,t_no):
    order=Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderitems=Orderitem.objects.filter(order=order)
    context={'orderitems':orderitems,'order':order}
    return render(request,'store/orders/view.html',context)