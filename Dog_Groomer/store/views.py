from django.shortcuts import render
from django.http import HttpResponse



def product_list(request):
    return HttpResponse("This is a page regarding products")

def product_detail(request):
    return HttpResponse("This is a page regarding product information")



