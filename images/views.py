from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import ImageCreateFrom

@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateFrom(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            new_image.user = request.user
            new_image.save()
            messages.success(request,'Image added successfully')
            return redirect(new_image.get_absolute_url())
    else:
        form = ImageCreateFrom(data=request.GET)
    return render(
        request,
        'images/image/create.html',
        {
            'section':'images',
            'form':form,
        }
    )