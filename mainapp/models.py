from django.db import models


class TrainingPlace(models.Model):
    training_place = models.CharField(verbose_name='место тренировок', max_length=128, unique=True)

    def __str__(self):
        return f'{self.training_place}'

    class Meta:
        verbose_name = 'место тренировок'
        verbose_name_plural = 'место тренировок'


class LevelTraining(models.Model):
    level_training = models.CharField(verbose_name='уровень подготовки', max_length=128, unique=True)

    def __str__(self):
        return f'{self.level_training}'

    class Meta:
        verbose_name = 'уровень подготовки'
        verbose_name_plural = 'уровень подготовки'


class Training(models.Model):
    name = models.CharField(verbose_name='тренировка', max_length=128, unique=True)
    purpose = models.CharField(verbose_name='цель', max_length=64)
    cycle_duration = models.IntegerField(verbose_name='длительность цикла')
    training_time_ot = models.IntegerField(verbose_name='время тренировки от')
    training_time_do = models.IntegerField(verbose_name='время тренировки до')
    training_place = models.ForeignKey(TrainingPlace,
                                  on_delete=models.CASCADE)
    training_sessions_per_week = models.IntegerField(verbose_name='тренировок в неделю')
    level_training = models.ForeignKey(LevelTraining,
                                  on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'тренировка'
        verbose_name_plural = 'тренировки'


class Weeks(models.Model):
    training = models.ForeignKey(Training,
                                  on_delete=models.CASCADE)
    week = models.IntegerField(verbose_name='неделя')
    monday = models.CharField(verbose_name='понедельник', max_length=64)
    tuesday = models.CharField(verbose_name='вторник', max_length=64)
    wednesday = models.CharField(verbose_name='среда', max_length=64)
    thursday = models.CharField(verbose_name='четверг', max_length=64)
    friday = models.CharField(verbose_name='пятница', max_length=64)
    saturday = models.CharField(verbose_name='суббота', max_length=64)
    sunday = models.CharField(verbose_name='воскресенье', max_length=64)

    def __str__(self):
        return f'{self.training}: {self.week}'

    class Meta:
        verbose_name = 'неделя'
        verbose_name_plural = 'недели'


class Day(models.Model):
    training = models.ForeignKey(Training,
                                 on_delete=models.CASCADE)
    weeks = models.ForeignKey(Weeks,
                                 on_delete=models.CASCADE)
    day = models.CharField(verbose_name='день', max_length=64)

    def __str__(self):
        return f'{self.weeks}/ {self.day}'

    class Meta:
        verbose_name = 'день'
        verbose_name_plural = 'дни'


class Exercises(models.Model):
    training = models.ForeignKey(Training,
                                 on_delete=models.CASCADE)
    day = models.ForeignKey(Day,
                              on_delete=models.CASCADE)
    name = models.CharField(verbose_name='упражнение', max_length=128)
    repetitions = models.IntegerField(verbose_name='повторений')
    approaches = models.IntegerField(verbose_name='повторов')
    rest = models.IntegerField(verbose_name='отдых (мин)')

    def __str__(self):
        return f'{self.day} / {self.name}'

    class Meta:
        verbose_name = 'упражнение'
        verbose_name_plural = 'упражнения'





