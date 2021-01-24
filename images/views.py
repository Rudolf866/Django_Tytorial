import redis
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views.decorators.http import require_POST

from images.forms import ImageCreateForm
from images.models import Image


r = redis.StrictRedis(host=sgitettings.REDIS_HOST,port=settings.REDIS_PORT,db=settings.REDIS_DB)


@login_required
def image_create(request):
    if request.method == 'POST':
        # Форма отправлена.
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # Данные формы валидны.
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            # Добавляем пользователя к созданному объекту.
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added successfully')
            # Перенаправляем пользователя на страницу сохраненного изображения.
            return redirect(new_item.get_absolute_url())
    else:
        # Заполняем форму данными из GET-запроса.
        form = ImageCreateForm(data=request.GET)
    return render(request, 'images/create.html', {'section': 'images', 'form': form})


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, 'images/detail.html', {'section': 'images', 'image': image})


@login_required
@require_POST
def image_like(request):
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
    return JsonResponse({'status': 'ok'})
