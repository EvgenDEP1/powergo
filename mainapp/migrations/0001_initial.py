# Generated by Django 3.2.7 on 2021-11-17 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='тренировка')),
                ('purpose', models.CharField(max_length=64, verbose_name='цель')),
                ('cycle_duration', models.IntegerField(max_length=2, verbose_name='длительность цикла')),
                ('training_time_ot', models.IntegerField(max_length=3, verbose_name='время тренировки от')),
                ('training_time_do', models.IntegerField(max_length=3, verbose_name='время тренировки до')),
                ('training_place', models.CharField(choices=[('H', 'Дом')], default='H', max_length=2, verbose_name='место тренировок')),
                ('training_sessions_per_week', models.IntegerField(max_length=2, verbose_name='длительность цикла')),
                ('level_training', models.CharField(choices=[('BE', 'Новичок')], default='BE', max_length=2, verbose_name='уровень подготовки')),
            ],
        ),
    ]
