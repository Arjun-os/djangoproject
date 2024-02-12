from idlelib import query

from django.db.models import Q
from django.shortcuts import render

from shop.models import Products


def search(request):
    query=""
    product=None
    if request.method=="POST":
        query=request.POST['q']
        if (query):
            product=Products.objects.filter(Q(name__icontains=query)|Q(desc__icontains=query))
    return render(request,template_name='search.html',context={'query':query,'p':product})