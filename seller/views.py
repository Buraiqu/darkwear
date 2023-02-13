from django.shortcuts import render

# Create your views here.
def seller_home(request):
    if request.method == 'POST':
        
        p_name = request.POST['productname']
        p_description = request.POST['description']
        p_category = request.POST['category']
        p_stock = request.POST['stock']
        p_price = request.POST['price']
        p_image = request.FILES['pic']
        seller = request.session['seller']

        p_product = Products(
            product_name= p_name,
            Description=  p_description,
            Category = p_category,
            Stock = p_stock,
            Price= p_price,
            p_image =  p_image,
            seller_id = seller
        )
        p_product.save()  
    return render(request,'seller_templates/seller_index.html')

def seller_variant(request):
    return render(request,'seller_templates/add_product_variant.html')

def seller_products(request):
    product_obj = Products.objects.filter(seller=request.session['seller'])
    return render(request,'seller_templates/seller_view.html',{'data':product_obj})
    return render(request,'seller_templates/seller_view.html')
    
def seller_change_password(request):
    msg = ''
    if request.method == 'POST':
        old_pass = request.POST['old']
        new_pass = request.POST['confirm']
        try:
            seller_obj = Seller.objects.get(id = request.session['seller'],password = old_pass)
            Seller.objects.filter(id = request.session['seller']).update(password = new_pass)
            msg = 'Change Successfull'
            return render(request,'seller_templates/change_password.html',{'message1':msg})
        except:
            msg = 'old Password does not match' 
            return render(request,'seller_templates/change_password.html',{'message':msg})
    return render(request,'seller_templates/change_password.html')

def seller_update_stock(request):
    pro = Products.objects.filter(seller_id=request.session['seller'])
    context = {
        'product':pro
    }
    return render(request,'seller_templates/stock_update.html',context)

def seller_stock_up(request):
    id = request.POST['pno']
    prod = Products.objects.filter(id = id).values('product_name','Stock')
    protitle = prod[0]['product_name']
    prostock = prod[0]['Stock']
    print(protitle)
    context = {
        'product_name':protitle,
        'Stock':prostock,
    }
    
    return JsonResponse(context)
    return render(request,'seller_templates/stock_update.html')

def seller_add_stock(request):
    new_stock =request.POST['new_stock']
    pno = request.POST['pno']
    prod = Products.objects.get(id = pno)
    pro = prod.Stock
    pro = pro +int(new_stock)
    Products.objects.filter(id= pno).update(Stock=pro)
    msg = 'Updated Successfully'
    context = {
        'message':msg,
    }
    return JsonResponse(context)    



def seller_profile(request):
    return render(request,'seller_templates/profile.html')