from django.shortcuts import render, HttpResponseRedirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def home(request):
  prod=Product.objects.all()
  for item in prod:
    item.discount=item.price-item.price*10/100
    item.save()
  if request.user.is_authenticated:
    item_cnt=CartItem.objects.filter(user=request.user).count()
  else:
    item_cnt=0

  q=request.GET.get('q') if request.GET.get('q')!=None else ''
  product=Product.objects.all()
  product=product.filter(Q(name__icontains=q))
  return render(request,'shop/home.html',{'product':product,'item_cnt':item_cnt})

def details(request,pk):
  product=Product.objects.get(name=pk)
  if request.user.is_authenticated:
    item_cnt=CartItem.objects.filter(user=request.user).count()
  else:
    item_cnt=0
  return render(request,'shop/details.html',{'product':product,'item_cnt':item_cnt})

def register(request):
  if request.method=="POST":
    user=request.POST['user']
    email=request.POST['email']
    pass1=request.POST['pass1']
    pass2=request.POST['pass2']
    if user!='' and email!='' and pass1!='' and pass2!='':
      if pass1==pass2:
        if User.objects.filter(username=user).exists():
          messages.info(request,'User already exists')
          return HttpResponseRedirect('/login/')
        elif User.objects.filter(email=email).exists():
          messages.info(request,'Email already exists')
          return HttpResponseRedirect('/login/')
        else:
          user1=User.objects.create_user(username=user,email=email,password=pass1)
          user1.save()
          return HttpResponseRedirect('/login/')
      else:
        messages.info(request,'Password mismatch')
        return HttpResponseRedirect('/register/')
    else:
      messages.info(request,'Please enter the fields')
      return HttpResponseRedirect('/register/')
  
  return render(request,'shop/register.html')

def login_page(request):
  if request.method=='POST':
    user=request.POST['user']
    pass1=request.POST['pass1']
    if User.objects.filter(username=user).exists():
      user=authenticate(request,username=user,password=pass1)
      if user is not None :
        login(request,user)
        return HttpResponseRedirect('/')
      else:
        messages.info(request,'Login Credentials Invalid')
        return HttpResponseRedirect('/login/')
    elif user=='':
        messages.info(request,'Please enter the fields')
        return HttpResponseRedirect('/login/')
    else:
      messages.info(request,"User doesn't exists")
      return HttpResponseRedirect('/register/')
  else:
    return render(request,'shop/login.html')

def logout_page(request):
  logout(request)
  return HttpResponseRedirect('/')


@login_required(login_url='/login/')
def view_cart(request):
  cart_items=CartItem.objects.filter(user=request.user)
  total_price=sum(item.total_price() for item in cart_items)
  item_cnt=cart_items.count() or 0
  if request.method=='POST':
    item_id=request.POST.get('item_id')
    action = request.POST.get('action')

    item = CartItem.objects.get(id=item_id, user=request.user)
    if action == 'dec' and item.quantity > 1:
        item.quantity -= 1
        
    elif action == 'inc' :
        item.quantity += 1
        
    item.save()
    return HttpResponseRedirect('/cart/')

  return render(request,'shop/cart.html',{'cart_items':cart_items,'total_price':total_price,'item_cnt':item_cnt})

@login_required(login_url='/login/')
def add_to_cart(request):
  if request.method=="POST":
    item_id=request.POST.get('item_id')
    product=Product.objects.get(id=item_id)
    cart_item,created=CartItem.objects.get_or_create(product=product,user=request.user)
    if not created:
      cart_item.quantity+=1
      cart_item.save()
    item_cnt=CartItem.objects.filter(user=request.user).count()
  return HttpResponseRedirect('/cart/')