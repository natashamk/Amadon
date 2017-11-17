from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'totalcount' not in request.session:
        request.session ['totalcount'] = 0
        'totalamount' not in request.session
        request.session ['totalamount'] = 0
    return render(request, 'amadonapp/index.html')

def process(request):
    # if quantity = 0:
    #     return redirect ('/checkout')
    prices = [19.99, 29.99, 4.99, 49.99]
    price = prices[int(request.POST['product_id'])]
    itemcount = float(request.POST['quantity'])
    itemvalue = price * itemcount
    request.session['itemvalue'] = itemvalue
    request.session['totalcount'] += itemcount
    request.session['totalamount'] += itemvalue

    return redirect('/checkout')

def checkout(request):
    return render(request,'amadonapp/checkout.html')

def goback(request):
    return redirect('/')