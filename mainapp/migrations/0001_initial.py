# Generated by Django 3.2.7 on 2021-11-18 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LevelTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_training', models.CharField(max_length=128, unique=True, verbose_name='уровень подготовки')),
            ],
            options={
                'verbose_name': 'уровень подготовки',
                'verbose_name_plural': 'уровень подготовки',
            },
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='тренировка')),
                ('purpose', models.CharField(max_length=64, verbose_name='цель')),
                ('cycle_duration', models.IntegerField(verbose_name='длительность цикла')),
                ('training_time_ot', models.IntegerField(verbose_name='время тренировки от')),
                ('training_time_do', models.IntegerField(verbose_name='время тренировки до')),
                ('training_sessions_per_week', models.IntegerField(verbose_name='тренировок в неделю')),
                ('level_training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.leveltraining')),
            ],
            options={
                'verbose_name': 'тренировка',
                'verbose_name_plural': 'тренировки',
            },
        ),
        migrations.CreateModel(
            name='TrainingPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_place', models.CharField(max_length=128, unique=True, verbose_name='место тренировок')),
            ],
            options={
                'verbose_name': 'место тренировок',
                'verbose_name_plural': 'место тренировок',
            },
        ),
        migrations.CreateModel(
            name='Weeks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField(verbose_name='неделя')),
                ('monday', models.CharField(max_length=64, verbose_name='понедельник')),
                ('tuesday', models.CharField(max_length=64, verbose_name='вторник')),
                ('wednesday', models.CharField(max_length=64, verbose_name='среда')),
                ('thursday', models.CharField(max_length=64, verbose_name='четверг')),
                ('friday', models.CharField(max_length=64, verbose_name='пятница')),
                ('saturday', models.CharField(max_length=64, verbose_name='суббота')),
                ('sunday', models.CharField(max_length=64, verbose_name='воскресенье')),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.training')),
            ],
            options={
                'verbose_name': 'тренировка',
                'verbose_name_plural': 'тренировки',
            },
        ),
        migrations.AddField(
            model_name='training',
            name='training_place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.trainingplace'),
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=64, verbose_name='день')),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.training')),
                ('weeks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.weeks')),
            ],
            options={
                'verbose_name': 'день',
                'verbose_name_plural': 'дни',
            },
        ),
    ]
