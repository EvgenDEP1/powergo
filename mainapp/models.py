from django.db import models


class TrainingPlace(models.TextChoices):
    HOME = 'H', 'Дом'


class LevelTraining(models.TextChoices):
    BEGINNER = 'BE', 'Новичок'


class Training(models.Model):
    name = models.CharField(verbose_name='тренировка', max_length=128, unique=True)
    purpose = models.CharField(verbose_name='цель', max_length=64)
    cycle_duration = models.IntegerField(verbose_name='длительность цикла')
    training_time_ot = models.IntegerField(verbose_name='время тренировки от')
    training_time_do = models.IntegerField(verbose_name='время тренировки до')
    training_place = models.CharField(verbose_name='место тренировок', max_length=2, choices=TrainingPlace.choices,
                                      default=TrainingPlace.HOME)
    training_sessions_per_week = models.IntegerField(verbose_name='тренировок в неделю')
    level_training = models.CharField(verbose_name='уровень подготовки', max_length=2, choices=LevelTraining.choices,
                                      default=LevelTraining.BEGINNER)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'тренировка'
        verbose_name_plural = 'тренировки'