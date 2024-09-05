from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import wigs
from .models import cart
from .models import cart_id
from .models import cart_wigs
from .models import bundle
from .models import single_drawn
from .models import double_drawn
from .models import superdouble_drawn
from .models import customer_details
from .forms import customer
from .models import bundlecart
from .forms import NewUserForm
from .forms import bundleform
from django.urls import reverse
import uuid
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random


def index(request):
    if 'user_uuid' not in request.session:
        request.session['user_uuid'] = uuid.uuid4().hex
    user_uuid = request.session['user_uuid']
    names=int(cart_wigs.objects.filter(username=user_uuid).count())
    bund=int(bundlecart.objects.filter(username=user_uuid).count())
    name=names+bund
    wig = bundle.objects.all().values()
    love= wigs.objects.all().values()
    random_items = random.sample(list(love), min(14, len(love)))
    random_wig = random.sample(list(wig), min(7, len(wig)))


    return render(request, 'index.html', {'love':random_items, "namecount":name, "soul": random_wig,})

@csrf_exempt
def bundlesprice(request,image1, id):
    wig = bundle.objects.get(id=id)
    love= bundle.objects.all().values()
    image=image1
    image_data = wig.image1.read()
    pricess = "you done it"
    return render(request, 'bundleimg.html', {"x":wig, 'image_obj': image_data, 'image':image, 'love':love, 'pricess':pricess})




def bundlesopen(request,image1, id):
    if request.method == "POST":
         texture = request.POST.get('choice_field')
         color = request.POST.get('choice_field4')
         if texture == "single":
             style = request.POST.get('choice_field2')
             if style =="natural":
                 length=request.POST.get('choice_field3')
                 bolaji = single_drawn.objects.get(length=length)
                 price = bolaji.price
                 life= f"Texture: {texture}, Style: {style}, color: {color}, Length: {length},  Price: ${price}"
                 wig = bundle.objects.get(id=id)
                 love= bundle.objects.all().values()
                 image=image1
                 image_data = wig.image1.read()
                 user_uuid = request.session['user_uuid']
                 cartsobjects = bundlecart()
                 cartsobjects.username=user_uuid
                 cartsobjects.image=image1
                 cartsobjects.product=life
                 cartsobjects.price=price
                 cartsobjects.save()
                 return render(request, 'bundleimg.html', {"x":wig, 'image_obj': image_data, 'image':image, 'love':love, 'forms':life})
             elif style == "bone" or style == "kinky":
                 length=request.POST.get('choice_field3')
                 bolaji = single_drawn.objects.get(length=length)
                 price = int(bolaji.price) + 8
                 life=f"Texture: {texture}, Style: {style}, color: {color}, Length: {length}, Price: ${price}"
                 wig = bundle.objects.get(id=id)
                 love= bundle.objects.all().values()
                 image=image1
                 image_data = wig.image1.read()
                 user_uuid = request.session['user_uuid']
                 cartsobjects = bundlecart()
                 cartsobjects.username=user_uuid
                 cartsobjects.image=image1
                 cartsobjects.product=life
                 cartsobjects.price=price
                 cartsobjects.save()
                 return render(request, 'bundleimg.html', {"x":wig, 'image_obj': image_data, 'image':image, 'love':love, 'forms':life})
             else:
                 length=request.POST.get('choice_field3')
                 bolaji = single_drawn.objects.get(length=length)
                 price = int(bolaji.price) + 3
                 life= f"Texture: {texture}, Style: {style}, color: {color}, Length: {length}, Price: ${price}"
                 wig = bundle.objects.get(id=id)
                 love= bundle.objects.all().values()
                 image=image1
                 image_data = wig.image1.read()
                 user_uuid = request.session['user_uuid']
                 cartsobjects = bundlecart()
                 cartsobjects.username=user_uuid
                 cartsobjects.image=image1
                 cartsobjects.product=life
                 cartsobjects.price=price
                 cartsobjects.save()
                 return render(request, 'bundleimg.html', {"x":wig, 'image_obj': image_data, 'image':image, 'love':love, 'forms':life})
         elif texture == "double":
             style = request.POST.get('choice_field2')
             if style =="natural":
                 length=request.POST.get('choice_field3')
                 bolaji = double_drawn.objects.get(length=length)
                 price = bolaji.price
                 life= f"Texture: {texture}, Style: {style}, color: {color}, Length: {length}, Price: ${price}"
                 wig = bundle.objects.get(id=id)
                 love= bundle.objects.all().values()
                 image=image1
                 image_data = wig.image1.read()
                 user_uuid = request.session['user_uuid']
                 cartsobjects = bundlecart()
                 cartsobjects.username=user_uuid
                 cartsobjects.image=image1
                 cartsobjects.product=life
                 cartsobjects.price=price
                 cartsobjects.save()
                 return render(request, 'bundleimg.html', {"x":wig, 'image_obj': image_data, 'image':image, 'love':love, 'forms':life})
             elif style == "bone" or style == "kinky":
                 length=request.POST.get('choice_field3')
                 bolaji = double_drawn.objects.get(length=length)
                 price = int(bolaji.price) + 8
                 life= f"Texture: {texture}, Style: {style}, color: {color}, Length: {length}, Price: ${price}"
                 wig = bundle.objects.get(id=id)
                 love= bundle.objects.all().values()
                 image=image1
                 image_data = wig.image1.read()
                 user_uuid = request.session['user_uuid']
                 cartsobjects = bundlecart()
                 cartsobjects.username=user_uuid
                 cartsobjects.image=image1
                 cartsobjects.product=life
                 cartsobjects.price=price
                 cartsobjects.save()
                 return render(request, 'bundleimg.html', {"x":wig, 'image_obj': image_data, 'image':image, 'love':love, 'forms':life})
             else:
                 length=request.POST.get('choice_field3')
                 bolaji = double_drawn.objects.get(length=length)
                 price = int(bolaji.price) + 3
                 life= f"Texture: {texture}, Style: {style}, color: {color}, Length: {length}, Price: ${price}"
                 wig = bundle.objects.get(id=id)
                 love= bundle.objects.all().values()
                 image=image1
                 image_data = wig.image1.read()
                 user_uuid = request.session['user_uuid']
                 cartsobjects = bundlecart()
                 cartsobjects.username=user_uuid
                 cartsobjects.image=image1
                 cartsobjects.product=life
                 cartsobjects.price=price
                 cartsobjects.save()
                 return render(request, 'bundleimg.html', {"x":wig, 'image_obj': image_data, 'image':image, 'love':love, 'forms':life})
         elif texture == "superdouble":
             style = request.POST.get('choice_field2')
             if style =="natural":
                 length=request.POST.get('choice_field3')
                 bolaji = superdouble_drawn.objects.get(length=length)
                 price = bolaji.price
                 life= f"Texture: {texture}, Style: {style}, color: {color}, Length: {length}, Price: ${price}"
                 wig = bundle.objects.get(id=id)
                 love= bundle.objects.all().values()
                 image=image1
                 image_data = wig.image1.read()
                 user_uuid = request.session['user_uuid']
                 cartsobjects = bundlecart()
                 cartsobjects.username=user_uuid
                 cartsobjects.image=image1
                 cartsobjects.product=life
                 cartsobjects.price=price
                 cartsobjects.save()
                 return render(request, 'bundleimg.html', {"x":wig, 'image_obj': image_data, 'image':image, 'love':love, 'forms':life})
             elif style == "bone" or style == "kinky":
                 length=request.POST.get('choice_field3')
                 bolaji = superdouble_drawn.objects.get(length=length)
                 price = int(bolaji.price) + 8
                 life= f"Texture: {texture}, Style: {style}, color: {color}, Length: {length}, Price: ${price}"
                 wig = bundle.objects.get(id=id)
                 love= bundle.objects.all().values()
                 image=image1
                 image_data = wig.image1.read()
                 user_uuid = request.session['user_uuid']
                 cartsobjects = bundlecart()
                 cartsobjects.username=user_uuid
                 cartsobjects.image=image1
                 cartsobjects.product=life
                 cartsobjects.price=price
                 cartsobjects.save()
                 return render(request, 'bundleimg.html', {"x":wig, 'image_obj': image_data, 'image':image, 'love':love, 'forms':life})
             else:
                 length=request.POST.get('choice_field3')
                 bolaji = superdouble_drawn.objects.get(length=length)
                 price = int(bolaji.price) + 3
                 life= f"Texture: {texture}, Style: {style}, color: {color}, Length: {length}, Price: ${price}"
                 wig = bundle.objects.get(id=id)
                 love= bundle.objects.all().values()
                 image=image1
                 image_data = wig.image1.read()
                 user_uuid = request.session['user_uuid']
                 cartsobjects = bundlecart()
                 cartsobjects.username=user_uuid
                 cartsobjects.image=image1
                 cartsobjects.product=life
                 cartsobjects.price=price
                 cartsobjects.save()
                 return render(request, 'bundleimg.html', {"x":wig, 'image_obj': image_data, 'image':image, 'love':love, 'forms':life})






    wig = bundle.objects.get(id=id)
    your_object = get_object_or_404( bundle, id=id)
    image2 = your_object.image2
    image3 = your_object.image3
    if 'user_uuid' not in request.session:
        request.session['user_uuid'] = uuid.uuid4().hex
    love= bundle.objects.all().values()
    image=image1
    add ="ADD TO CART"
    image_data = wig.image1.read()
    forms= bundleform
    user_uuid = request.session['user_uuid']
    names=int(cart_wigs.objects.filter(username=user_uuid).count())
    bund=int(bundlecart.objects.filter(username=user_uuid).count())
    name=names+bund
    return render(request, 'bundleimg.html', {"x":wig, 'image_obj': image_data,"namecount":name, 'image':image, 'love':love, 'forms':forms, 'add':add, 'image2':image2, 'image3':image3})


def bundles(request):
    if 'user_uuid' not in request.session:
       request.session['user_uuid'] = uuid.uuid4().hex
    user_uuid = request.session['user_uuid']
    wig = bundle.objects.all().values()
    names=int(cart_wigs.objects.filter(username=user_uuid).count())
    bund=int(bundlecart.objects.filter(username=user_uuid).count())
    name=names+bund
    return render(request, 'bundleshop.html', {"wigs":wig, "namecount":name})



def checkout(request):
    if request.method == "POST":
        if 'user_uuid' not in request.session:
            request.session['user_uuid'] = uuid.uuid4().hex
        user_uuid = request.session['user_uuid']
        users = user_uuid
        bundle_model= bundlecart.objects.filter(username=users)
        bolaji_model = cart_wigs.objects.filter(username=users)
        total_bundle = sum(item.price for item in  bundle_model)
        total_price = sum(item.price for item in bolaji_model)
        total= int(total_bundle + total_price)
        price= int(total_bundle + total_price)
        bundle = bundlecart.objects.all().values()
        username=user_uuid
        wig = cart_wigs.objects.all().values()
        name_wig=cart_wigs.objects.filter(username=users).count()
        name_bundle=bundlecart.objects.filter(username=users).count()
        name=int(name_wig+name_bundle)
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        address=request.POST.get("address")
        state=request.POST.get("state")
        country=request.POST.get("country")
        person ="we received your order"
        subject = 'Order from Hairbypeace'
        message = 'We have received your order, we are currently processing it. A representative will contact you thank you'
        from_email = 'trustallianceng@gmail.com'
        recipient_list = [email, 'daropaleb@gmail.com']
        recipient_name = f"{person} thank you please comeback again {phone}. {address}, {state}, {country}. "  # Replace with the actual recipient name
        html_message = render(request, 'userpage.html', {"register_form":recipient_name, "wigs":wig, "bundle":bundle, 'total': total,  "namecount":name, 'users':users}).content.decode('utf-8')
        send_mail(subject, message, from_email, recipient_list, html_message=html_message)
        my_model = customer_details(username=username, price=price, phone=phone, email=email, state=state, country=country)
        my_model.save()
        return render(request, 'userpage.html', {"wigs":wig, "bundle":bundle, 'total': total,  "namecount":name, 'users':users, 'register_form':recipient_name})


    if 'user_uuid' not in request.session:
        request.session['user_uuid'] = uuid.uuid4().hex
    user_uuid = request.session['user_uuid']
    users = user_uuid
    wig = cart_wigs.objects.all().values()
    bundle = bundlecart.objects.all().values()
    bundle_model= bundlecart.objects.filter(username=users)
    bolaji_model = cart_wigs.objects.filter(username=users)
    total_bundle = sum(item.price for item in  bundle_model)
    total_price = sum(item.price for item in bolaji_model)
    total= int(total_bundle + total_price)
    name_wig=cart_wigs.objects.filter(username=users).count()
    name_bundle=bundlecart.objects.filter(username=users).count()
    name=int(name_wig+name_bundle)
    form= customer()
    life="Submit"
    return render(request, 'userpage.html', {"wigs":wig, "bundle":bundle, 'total': total,  "namecount":name, 'users':users, 'register_form':form, 'life':life})

def delete_item(request, id):
    item = get_object_or_404(cart_wigs, id=id)
    item.delete()
    return redirect('checkout')
def delete_bundle(request, id):
    item = get_object_or_404(bundlecart, id=id)
    item.delete()
    return redirect('checkout')


def ligs(request):
    if 'user_uuid' not in request.session:
        request.session['user_uuid'] = uuid.uuid4().hex
    user_uuid = request.session['user_uuid']
    wig = wigs.objects.all().values()
    names=int(cart_wigs.objects.filter(username=user_uuid).count())
    bund=int(bundlecart.objects.filter(username=user_uuid).count())
    name=names+bund

    return render(request, 'shop.html', {"wigs":wig, "namecount":name})



def shops(request, id ):
    if 'user_uuid' not in request.session:
        request.session['user_uuid'] = uuid.uuid4().hex
    user_uuid = request.session['user_uuid']
    ide = wigs.objects.get(id=id)
    cartsobjects = cart_wigs()
    cartsobjects.username=user_uuid
    cartsobjects.item_name= ide.item_name
    cartsobjects.price= ide.price
    cartsobjects.number= ide.number
    cartsobjects.item_colour=ide.item_colour
    cartsobjects.item_length=ide.item_length
    cartsobjects.image1=ide.image1
    cartsobjects.save()
    return redirect('ligs')





def opencart(request,image1, id):
    wig = wigs.objects.get(id=id)
    love= wigs.objects.all().values()
    random_items = random.sample(list(love), min(10, len(love)))
    image=image1
    image_data = wig.image1.read()
    return render(request, 'testimonial.html', {"x":wig, 'image_obj': image_data, 'image':image, 'love':random_items})

def carts(request, id):
    response = HttpResponse("Cookie set!")
    response.set_cookie('user_id', id, max_age=16000)
    wig = wigs.objects.all().values()
    return render(request, 'shop.html', {"wigs":wig})



def user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)


                welcome = f" {username}."
                return redirect('/shop')


            else:
                 form = "Invalid Username or Password"
                 return render(request=request, template_name="why.html", context={"register_form":form})

        else:
             form = "Invalid Username or Password"
             return render(request=request, template_name="why.html", context={"register_form":form})
    form = AuthenticationForm()
    create = "new/"
    used = "Create New User"
    life = "Login"
    ball="Login"
    return render(request, "why.html", {"register_form":form,  'new':create, 'used':used, 'life':life, 'all':ball})

def new(request):
   if request.method == "POST":
       form = NewUserForm(request.POST)
       if form.is_valid():
           user = form.save()
           return redirect('/login/')

   form= NewUserForm()
   life= "Create"
   used = "Already have account Login here "
   ball="Create New User"

   return render(request=request, template_name="why.html", context={"register_form":form, 'life':life, 'login':used, 'all':ball})








# Create your views here.
