from django.core.management.base import BaseCommand

from mainapp.models import TrainingPlace


class Command(BaseCommand):
    def handle(self, *args, **options):
        item = 0
        while item <= 4:
            TrainingPlace.objects.get_or_create(
                training_place=f'место тренировок {item + 1}',
            )
            item += 1
        print('Места тренировок созданы')
