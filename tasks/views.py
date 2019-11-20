from django.shortcuts import render, redirect
from .forms import ItemForm
from django.contrib import auth, messages

# Create your views here.
def create_item(request):
    if request.method == "POST":
        #create form and fill it with user input
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'New item has been successfully added')
            return redirect(create_item)
        else:
            return render(request,'tasks/create_item.html',{
                'form':form
            })
    else:
        form = ItemForm()
        return render(request,'tasks/create_item.html',{
            'form':form
        })