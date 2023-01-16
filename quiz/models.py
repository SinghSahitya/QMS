from django.db import models
from django.contrib.auth.models import User

class QuizCategory(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField()
    image = models.ImageField(upload_to='cat_imgs/')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class QuizQuestion(models.Model):
    category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    question = models.CharField(max_length=200, null=True)
    op1 = models.CharField(max_length=200, null=True)
    op2 = models.CharField(max_length=200, null=True)
    op3 = models.CharField(max_length=200, null=True)
    op4 = models.CharField(max_length=200, null=True)
    right_opt = models.CharField(max_length=200, null=True)
    level = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Questions'


    def __str__(self):
        return self.question
        
class UserSubmittedAnswer(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    right_answer=models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural='User Submitted Answers'

        
class UserCategoryAttempts(models.Model):
    category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    attempt_time=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural='User Attempts Category'