from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from basketapp.models import TrainingBasket
from django.urls import reverse

from mainapp.models import Training

from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    items = TrainingBasket.objects.filter(user=request.user)
    context = {
        'object_list': items,
    }

    return render(request, 'basketapp/basket.html', context)


def add(request, training_id):
    training = Training.objects.get(pk=training_id)
    TrainingBasket.objects.get_or_create(
        user=request.user,
        training=training
    )

    return HttpResponseRedirect(reverse('mainapp:training_page',
                                        kwargs={'pk': training.id}))


def remove(request, training_basket_id):
    if request.is_ajax():
        item = TrainingBasket.objects.get(id=training_basket_id)
        item.delete()
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return JsonResponse({'status': 'ok',
                             'training_basket_id': training_basket_id})
