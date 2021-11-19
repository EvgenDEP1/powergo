from django.contrib import admin

from mainapp.models import Training, TrainingPlace, LevelTraining, Weeks, Day, Exercises

admin.site.register(Training)
admin.site.register(TrainingPlace)
admin.site.register(LevelTraining)
admin.site.register(Weeks)
admin.site.register(Day)
admin.site.register(Exercises)


