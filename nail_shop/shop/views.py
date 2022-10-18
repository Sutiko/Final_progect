from itertools import product
from django.shortcuts import render
from .models import Product, Firm

def args_dictionary(req):
    products_amount = Product.objects.count()
    firm_amount = Firm.objects.count()
    visits = req.session.get('visits',0)
    
    return {'visits' : visits,
            'products_amount' : products_amount,
            'firm_amount' : firm_amount,
            }

def base(request):
    products_amount = Product.objects.count()
    firm_amount = Firm.objects.count()
    return render (request, 'base.html', {'products_amount': products_amount,
                                            'firms_amount' : firm_amount})

def shop(request):
    request.session['visits'] = request.session.get('visits',0) + 1
    dictionary = args_dictionary(request)
    dictionary['products'] = Product.objects.all()
    return render(request, 'shop.html', dictionary)

def product(request, id):
    dictionary = args_dictionary(request)
    dictionary['products'] = Product.objects.get(id=id)
    return render (request, 'view.html', dictionary)

def buy(request, id):
    dictionary = args_dictionary(request)
    dictionary['products'] = Product.objects.get(id=id)
    return render (request, 'buy.html', dictionary)   

