from django.core.paginator import Paginator, EmptyPage, \
    PageNotAnInteger
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods

from common.decorators import ajax_required
from .forms import ImageCreateForm
from .models import Image

login_required


@login_required
def image_create(request):
    """view for creating image"""
    if request.method == 'POST':
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            print('asdfasdfasdfasdf**************')
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            messages.success(request, "Image was added successfully")
            return redirect(new_item.get_absolute_url())
    else:
        form = ImageCreateForm(data=request.GET)
    return render(request,
                  'images/image/create.html',
                  {'section': 'images',
                   'form': form})


def image_detail(request, id, slug):
    """detial view of specific image"""
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, 'images/image/detail.html',
                  {'section': 'image',
                   'image': image})


@ajax_required
@login_required
@require_http_methods(['POST'])
def image_like(request):
    """Liking/disliking image view"""
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except:
            pass
        return JsonResponse({'status': 'error'})


@login_required
def image_list(request):
    """Retrieve image list by normal request or ajax"""
    images = Image.objects.all()
    paginator = Paginator(images, 8)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            return HttpResponse('')
        images = paginator.page(Paginator.num_pages)
    context = {'section': 'images', 'images': images}
    if request.is_ajax():
        return render(request,
                      'images/image/list_ajax.html',
                      context=context)
    return render(request,
                  'images/image/list.html',
                  context=context)
