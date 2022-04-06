from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from basketapp.models import TrainingBasket
from django.urls import reverse

from mainapp.models import Training

from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    object_list = TrainingBasket.objects.filter(user=request.user)
    context = {
        'object_list': object_list,
    }

    return render(request, 'basketapp/basket.html', context)


def add(request, training_id):
    if not request.user.is_authenticated:
        return JsonResponse({
            'status': False,
            'message': 'Авторизуйтесь, чтобы добавить товар в избранное!'
        })
    trainings = Training.objects.get(pk=training_id)
    tra_object, creaated = TrainingBasket.objects.get_or_create(
        user=request.user,
        training=trainings
    )
    if creaated:
        return JsonResponse({
            'status': True,
            'id': trainings.id,
            'message': 'Вы успешно добавили товар в избранное!'
        })
    return JsonResponse({
        'status': False,
        'message': 'Товар уже в избранном!'
    })

    # return HttpResponseRedirect(reverse('mainapp:training_page',
    #                                     kwargs={'pk': training.id}))


def remove(request, training_basket_id):
    # if request.is_ajax():
    item = TrainingBasket.objects.get(id=training_basket_id)
    item.delete()
    return HttpResponseRedirect(reverse('basketapp:index'))
        # return JsonResponse({'status': 'ok',
        #                      'training_basket_id': training_basket_id})
