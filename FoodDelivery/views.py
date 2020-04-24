from random import random
import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.shortcuts import render, render_to_response,redirect
from django.template import RequestContext
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from.models import user_details,products,order_details,orders
from django.views.decorators.csrf import csrf_protect
import string
import random
import datetime

def id_generator(size=32, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def login(request):
    c={}
    c.update(csrf(request))
    return render(request,"login.html",c)

def addproduct(request):
    c = {}
    c.update(csrf(request))
    if request.session.get("username")=="admin":
        if(request.POST.get("add",'')):
            pid=request.POST.get("pid")
            name=request.POST.get("name")
            price=request.POST.get("price")
            category=request.POST.get("category")
            image=request.POST.get("image")
            print(pid)
            if products.objects.filter(pid=pid).exists():
                c['msg']="PID already taken"
                return render(request, "addproduct.html", c)
            else:
                p=products(pid=pid,name=name,price=price,image=image,category=category)
                p.save()
                return HttpResponseRedirect("/FoodDelivery/viewproducts", c)
        else:
            return render(request, "addproduct.html", c)
    else:
        return HttpResponseRedirect("/FoodDelivery/login", c)

def deleteproduct(request):
    c={}
    pid=request.GET.get('pid','')
    if request.session.get("username")=="admin":
        products.objects.filter(pid=pid).delete()
        return HttpResponseRedirect("/FoodDelivery/viewproducts",c)
    else:
        return HttpResponseRedirect("/FoodDelivery/login", c)

def updateproduct(request):
    c={}
    c = {"request": request}
    c.update(csrf(request))
    if request.session.get("username")=="admin":
        if(request.POST.get("update")):
            pid=request.POST.get("pid")
            print(pid)
            name=request.POST.get("name")
            price=request.POST.get("price")
            print(price)
            image=request.POST.get("image")
            category=request.POST.get("category")
            pid=request.POST.get("pid")
            p = products.objects.all().filter(pid=pid)
            for t in p:
                t.name =name
                t.price =price
                t.image = image
                t.category =category
                t.save()
            return HttpResponseRedirect("/FoodDelivery/viewproducts",c)
        else:
            pid = request.GET.get('pid', '')
            q = products.objects.filter(pid=pid)
            c['obj'] = q
            return render(request,"updateproduct.html",c)
    else:
        return HttpResponseRedirect("/FoodDelivery/login", c)

def viewproducts(request):
    c={}
    if request.session.get("username")=="admin":
        p=products.objects.all()
        return render(request,"viewproducts.html",{'obj':p})
    else:
        return HttpResponseRedirect("/FoodDelivery/login", c)

def vieworders(request):
    c={}
    if request.session.get("username")=="admin":
        q = orders.objects.all()
        return render(request, "vieworders.html", {'obj': q})
    else:
        return HttpResponseRedirect("/FoodDelivery/login", c)

@csrf_protect
def auth_view(request):
    context = {}
    uname = request.POST.get('username', False)
    pwd = request.POST.get('password', False)
    if uname=='admin' and pwd=='admin':
        c = {}
        c.update(csrf(request))
        request.session['username'] ="admin"
        return render(request, "admin.html", c)
    if user_details.objects.filter(username=uname).exists() and user_details.objects.get(username=uname).password == pwd:
        request.session['username'] = uname
        request.session['firstname'] = user_details.objects.get(username=uname).firstname.title()
        request.session['lastname'] = user_details.objects.get(username=uname).lastname.title()
        request.session['mobile'] = user_details.objects.get(username=uname).mobile
        request.session['address'] = user_details.objects.get(username=uname).address
        request.session['email'] = user_details.objects.get(username=uname).email
        # request.session['cart_count'] = get_cart_count(email)
        request.session['cart']={}
        request.session.save()
        context['request'] =request
        # context['image']='/img/burger.jpg'
        return HttpResponseRedirect("/FoodDelivery/Menu?category=mains",context)
    else:

        context['msg']="Invalid Username/Password"
        return render(request,"login.html",context)



def logout(request):
    c={}
    if request.session.get('username'):
        request.session.flush()
    return HttpResponseRedirect("login.html",c)

def MyAccount(request):
    c={"request":request}
    c.update(csrf(request))
    if(request.session.get("username")):
        c['username']=request.session.get('username')
        c['firstname']=request.session.get('firstname')
        c['lastname']=request.session.get('lastname')
        c['address']=request.session.get('address')
        c['mobile']=request.session.get('mobile')
        c['email']=request.session.get('email')
        return render_to_response('MyAccount.html',c)
    else:
        return render_to_response('login.html', c)

def Delete(request):
    c={"request":request}
    username=request.session.get('username')
    if (request.session.get("username")):
        request.session.flush()
        user_details.objects.filter(username=username).delete()
        return HttpResponseRedirect("../Menu?category=mains",c)
    else:
        return render_to_response("login.html", c)
@csrf_protect
def Edit(request):
    c={"request":request}
    c.update(csrf(request))
    if (request.session.get("username")):

        if (request.POST.get("update")):
            uname=request.session.get('username')
            request.session['firstname']= request.POST.get('firstname', '')
            request.session['lastname']= request.POST.get('lastname', '')
            request.session['email']= request.POST.get('email', '')
            request.session['mobile']= request.POST.get('mobile', '')
            request.session['address']= request.POST.get('address', '')
            u = user_details.objects.filter(username=uname)
            for t in u:
                t.firstname=request.session.get('firstname')
                t.lastname=request.session.get('lastname')
                t.email=request.session.get('email')
                t.mobile=request.session.get('mobile')
                t.address=request.session.get('address')
                t.save()
            c['username'] = request.session.get('username')
            c['firstname'] = request.session.get('firstname')
            c['lastname'] = request.session.get('lastname')
            c['address'] = request.session.get('address')
            c['mobile'] = request.session.get('mobile')
            c['email'] = request.session.get('email')
            return render_to_response("MyAccount.html", c)
        else:
            c['username'] = request.session.get('username')
            c['firstname'] = request.session.get('firstname')
            c['lastname'] = request.session.get('lastname')
            c['address'] = request.session.get('address')
            c['mobile'] = request.session.get('mobile')
            c['email'] = request.session.get('email')
            return render_to_response("Edit.html", c)
    else:
        return HttpResponseRedirect("../Menu?category=mains",c)

def MyOrders(request):
    c={'request':request}
    orderss={}
    order={}
    all_orders={}
    username=request.session.get('username')
    order_ids=orders.objects.all().filter(username=username)
    # print(order_ids)
    for orderid in order_ids:
        products=order_details.objects.all().filter(order_id=orderid.order_id)
        for product in products:
            order[product.pid]={'image':product.image,'name':product.name,'quantity':product.quantity,'price':product.price}
        orderss['items1']=order
        orderss['total']=orderid.total
        orderss['date']=orderid.date
        orderss['address']=orderid.delivery_address
        all_orders[orderid.order_id]=orderss
    c['all']=all_orders
    return render(request,"myorder.html",c)

def AboutUs(request):
    c={}
    return render(request,"about_us.html",c)

def Menu(request):
    if request.GET.get('action','')=='add':
        pid = request.GET.get('pid', '')
        cart=request.session.get('cart')
        name=products.objects.get(pid=pid).name
        price=products.objects.get(pid=pid).price
        image=products.objects.get(pid=pid).image
        if not (cart):
            product = {"name": name, "pid": pid, "quantity": 1, "price": price, "item_total":price,"image": image}
            cart ={pid: product}
        else:
            if pid in cart:
                cart[pid]["quantity"]+=1
                cart[pid]["item_total"]+=price
            else:
                product = {"name": name, "pid": pid, "quantity": 1, "price": price, "item_total":price, "image": image}
                cart[pid] =product
        print(cart)
        request.session['cart'] = cart


    category=request.GET.get('category','')
    query=products.objects.all().filter(category=category)
    return render(request,"Menu.html",{'obj':query})

def Order(request):
    if(request.session.get("username")):
        c={"request":request}
        cart=request.session.get("cart")
        c.update(csrf(request))
        c["cart"]=cart
        if not cart:
            return HttpResponseRedirect("../Menu?category=mains",c)
        else:
            order_id = id_generator()
            print(order_id)
            uname = request.session.get("username")
            address=request.session.get("address")
            grand_total=request.session.get("grand_total")
            ddate=datetime.date.today()
            c["total"]=request.session.get("total")
            c["grand_total"]=request.session.get("grand_total")
            c["tax"]=request.session.get("tax")
            order=orders(username=uname,order_id=order_id,delivery_address=address,date=ddate,total=grand_total)
            order.save()
            sender_email = "gadarajainik1@gmail.com"
            password = "Gadara@851999"
            receiver_email=request.session.get("email")
            subject = "Order-ID" + order_id
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = request.session.get("email")
            message["Subject"] = subject
            body="Your Order was successfully placed with total: Rs."+str(grand_total)
            message.attach(MIMEText(body, "plain"))
            text = message.as_string()
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, text)
            for obj in cart:
                order_detail=order_details(order_id=order_id, pid=obj,quantity=cart[obj]["quantity"],name=cart[obj]["name"],price=cart[obj]["price"],image=cart[obj]["image"])
                order_detail.save()
            del request.session["cart"]
            return render(request,"order.html",c)

def Register(request):
    c={}
    c.update(csrf(request))
    return render_to_response("Register.html",c)

def Transaction(request):
    c={"request":request}
    cart=request.session.get("cart")
    if(not cart):
        return HttpResponseRedirect('/FoodDelivery/Menu?category=mains',c)
    if(request.session.get('username')):
        if(request.POST.get('edit')):
            c.update(csrf(request))
            c["edit"]=True
            c["cart"] = request.session.get("cart")
            c["name"] = request.session.get("firstname")+" "+request.session.get("lastname")
            c["address"] = request.session.get("address")
            c["total"] = request.session.get("total")
            c["tax"] = request.session.get("tax")
            c["grand_total"] = request.session.get("grand_total")
            return render_to_response('transaction.html',c)
        if(request.POST.get('save')):
            c.update(csrf(request))
            c["cart"] = request.session.get("cart")
            c['address']=request.POST.get('add')
            c["name"] = request.POST.get('name')
            c["total"] = request.session.get("total")
            c["tax"] = request.session.get("tax")
            c["grand_total"] = request.session.get("grand_total")
            return render_to_response('transaction.html', c)
        else:
            c.update(csrf(request))
            c["cart"]=request.session.get("cart")
            c["name"]=request.session.get("firstname")+" "+request.session.get("lastname")
            c["address"]=request.session.get("address")
            c["total"]=request.session.get("total")
            c["tax"]=request.session.get("tax")
            c["grand_total"]=request.session.get("grand_total")
            return render_to_response('transaction.html', c)

def Cart(request):

    c={"request":request}
    c.update(csrf(request))
    sum=0
    if request.session.get('username'):
        cart=request.session.get('cart')
        print(cart)
        if not cart:
            c["empty"]=True
            return render_to_response("Cart.html",c)
        else:

            if request.GET.get('action')=="remove" and request.GET.get('pid'):
                pid=request.GET.get('pid')
                if cart[pid]["quantity"]>1:
                    cart[pid]["quantity"]-=1
                    cart[pid]["item_total"]-=cart[pid]["price"]
                    request.session['cart']=cart
                elif cart[pid]["quantity"]==1:
                    pid = request.GET.get('pid')
                    del cart[pid]
                    request.session['cart'] = cart
            elif request.GET.get('action')=="add" and request.GET.get('pid'):
                pid=request.GET.get('pid')
                cart[pid]["quantity"]+= 1
                cart[pid]["item_total"] += cart[pid]["price"]
                request.session['cart'] = cart
            elif request.GET.get('action')=="delete" and request.GET.get('pid'):
                pid = request.GET.get('pid')
                del cart[pid]
                request.session['cart'] = cart
            for obj in cart:
                print(obj)
                sum = sum + ((cart[obj]["quantity"]) * (cart[obj]["price"]))
            if sum>0:
                tax = 0.05 * sum
                grand_total = sum + tax
                c["grand_total"] = grand_total
                c["tax"] = tax
                c["total"] = sum
                c["cart"]=cart
                request.session["grand_total"]=grand_total
                request.session["tax"]=tax
                request.session["total"]=sum
                return render_to_response('Cart.html',c)
            else:
                c["empty"] = True
                return render_to_response("Cart.html", c)
    else:
            return HttpResponseRedirect('/FoodDelivery/login',c)

def adduser_details(request):
    c = {}
    c['msg']=""
    c.update(csrf(request))
    uname=request.POST.get('username','')
    pwd=request.POST.get('pwd','')
    rpwd = request.POST.get('rpwd', '')
    fname=request.POST.get('fname','')
    lname=request.POST.get('lname','')
    email=request.POST.get('email','')
    mobile=request.POST.get('mobile', '')
    add=request.POST.get('address','')
    t=user_details.objects.filter(username=uname).exists()
    if  not t:
        if rpwd == pwd:
            t = user_details(username=uname, password=pwd, firstname=fname, lastname=lname, mobile=mobile, email=email,address=add)
            t.save()
            c['msg'] = "Account created!!!"
            return render(request,"login.html", c)
        else:
            c['msg'] = "Passwords doesn't match!!!"
            return render(request,"Register.html", c)

    else:
        c['msg'] = "Username already taken!!!"
        return render(request,"Register.html", c)




def logout(request):
    if request.session.get('username'):
            auth.logout(request)
            request.session.flush()
            return HttpResponseRedirect('/FoodDelivery/login')
    else:
        return HttpResponseRedirect('/FoodDelivery/login')
