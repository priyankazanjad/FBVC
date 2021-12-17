from django.shortcuts import render,redirect
from .forms import LaptopModelForm
from .models import Laptop

def addlaptopmodel(request):
    form = LaptopModelForm()
    if request.method == 'POST':
        form = LaptopModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_laptop')
    template_name = 'LaptopApp/addlaptop.html'
    context = {'form':form}
    return render(request,template_name,context)

def showlaptop(request):
    laptop = Laptop.objects.all()
    context = {'laptop':laptop}
    template_name = 'LaptopApp/showlaptop.html'
    return render(request,template_name,context)

def deletelaptop(request,i):
    laptop = Laptop.objects.get(id=i)
    if request.method == 'POST':
        laptop.delete()
        return redirect('show_laptop')
    context = {'laptop':laptop}
    template_name = 'LaptopApp/deletelaptop.html'
    return render(request,template_name,context)

def updatelaptop(request,i):
    laptop = Laptop.objects.get(id=i)
    form = LaptopModelForm(instance=laptop)
    if request.method == 'POST':
        form = LaptopModelForm(request.POST,instance=laptop)
        if form.is_valid():
            form.save()
            return redirect('show_laptop')
    context = {'form':form}
    template_name = 'LaptopApp/addlaptop.html'
    return render(request,template_name,context)


# Create your views here.
