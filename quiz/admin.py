from django.contrib import admin
from . import models

admin.site.register(models.QuizCategory)

class QuizQuestionAdmin(admin.ModelAdmin):
    list_display=['question', 'level']
admin.site.register(models.QuizQuestion, QuizQuestionAdmin)

class UserSubmittedAnswerAdmin(admin.ModelAdmin):
    list_display=['id', 'question', 'user', 'right_answer']
admin.site.register(models.UserSubmittedAnswer,UserSubmittedAnswerAdmin)

class UserCategoryAttemptsAdmin(admin.ModelAdmin):
    list_display=['category', 'user', 'attempt_time']
admin.site.register(models.UserCategoryAttempts, UserCategoryAttemptsAdmin)
