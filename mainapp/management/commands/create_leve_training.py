from django.core.management.base import BaseCommand

from mainapp.models import LevelTraining


class Command(BaseCommand):
    def handle(self, *args, **options):
        item = 0
        while item <= 4:
            LevelTraining.objects.get_or_create(
                level_training=f'уровень подготовки {item + 1}',
            )
            item += 1
        print('Уровни подготовки созданы')
