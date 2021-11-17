from django.contrib import admin

from mainapp.models import Training, TrainingPlace, LevelTraining, Weeks

admin.site.register(Training)
admin.site.register(TrainingPlace)
admin.site.register(LevelTraining)
admin.site.register(Weeks)


