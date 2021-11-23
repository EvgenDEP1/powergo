from django.db import models
from django_summernote.fields import SummernoteTextField


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
    text = SummernoteTextField(verbose_name='о программе')
    img = models.ImageField(verbose_name='превью', upload_to='img/training_list/')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'тренировка'
        verbose_name_plural = 'тренировки'


class Weeks(models.Model):
    training = models.ForeignKey(Training,
                                  on_delete=models.CASCADE)
    week = models.IntegerField(verbose_name='неделя')

    def __str__(self):
        return f'{self.training}: {self.week} неделя'

    class Meta:
        verbose_name = 'неделя'
        verbose_name_plural = 'недели'


class Category(models.TextChoices):
    MONDAY = 'MO', 'понедельник'
    TUESDAY = 'TU', 'вторник'
    WEDNESDAY = 'WE', 'среда'
    THURSDAY = 'TH', 'четверг'
    FRIDAY = 'FR', 'пятница'
    SATURDAY = 'SA', 'суббота'
    SUNDAY = 'SU', 'воскресенье'
    # WEEKEND = "WD", 'день отдыха'
    # DAY = 'DA', models.CharField()


class Day(models.Model):
    training = models.ForeignKey(Training,
                                 on_delete=models.CASCADE)
    weeks = models.ForeignKey(Weeks,
                                 on_delete=models.CASCADE)
    category = models.CharField(max_length=2, choices=Category.choices,
                                verbose_name='день недели')
    day = models.IntegerField(verbose_name='день')

    def __str__(self):
        return f'{self.training} / {self.weeks} неделя / {self.day} день'

    class Meta:
        verbose_name = 'день'
        verbose_name_plural = 'дни'


class Exercises(models.Model):
    training = models.ForeignKey(Training,
                                 on_delete=models.CASCADE)
    day = models.ForeignKey(Day,
                              on_delete=models.CASCADE)
    name = models.CharField(verbose_name='упражнение', max_length=128)
    img = models.ImageField(verbose_name='превью', upload_to='img/')
    video = models.FileField(verbose_name='видео', upload_to='video/')
    repetitions = models.IntegerField(verbose_name='повторений')
    approaches = models.IntegerField(verbose_name='повторов')
    rest = models.IntegerField(verbose_name='отдых (мин)')

    def __str__(self):
        return f'{self.day} / {self.name}'

    class Meta:
        verbose_name = 'упражнение'
        verbose_name_plural = 'упражнения'





