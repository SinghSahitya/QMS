from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns= [
    path('', views.all_categories, name='all_categories'),
    path('accounts/register', views.register, name='quiz-register'),
    path('all-categories', views.all_categories, name='all_categories'),
    path('category_questions/<int:cat_id>', views.category_questions, name='category_questions'),
    path('submit-answer/<int:cat_id>/<int:quest_id>', views.submit_answer, name='submit_answer'),
    path('result_page/', views.result_page, name='result'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
