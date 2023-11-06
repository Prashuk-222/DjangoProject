from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
# Create your views here.

def receipes(request):
    data = request.POST
    if request.method == "POST":
        data=request.POST
        receipe_name = data.get('receipe_name')
        receipe_description =data.get('receipe_description')
        rimage=request.FILES.get('receipe_image')
        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=rimage,
        )
        return redirect('/receipes/')   
    queryset = Receipe.objects.all()
    context = {'receipes': queryset}
    return render(request,"receipes.html",context)

def delete_receipe(request,id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes/') 
def update_receipe(request,id):
    queryset = Receipe.objects.get(id=id)
    context = {'re': queryset}
    if request.method=="POST":
        data=request.POST
        receipe_name = data.get('receipe_name')
        receipe_description =data.get('receipe_description')
        rimage=request.FILES.get('receipe_image')

        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description
        
        
        if rimage:
            queryset.receipe_image=rimage
        
        queryset.save()
        return redirect('/receipes/') 
    return render(request,"update.html",context)