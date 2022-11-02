from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'exam'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_api, name='register'),
    path('login/', views.login_api, name='login'),
    path('question/list/', views.Question_list_api, name='list_question'),
    path('question/update/<int:pk>/', views.Question_api_detail, name='update_question'),
    path('question/delete/<int:pk>/', views.Question_api_detail, name='delete_question'),
    path('exam/create/list', views.Exam_list_api, name= 'exam'),
    path('exams/<int:pk>/', views.Exam_api_detail),
    # path('exam/submit/', views.store_result_api, name='submit_exam'),

    # # admin api
    # path('question/upload/', views.upload_question_api, name='upload_question'),
    # path('result/list/', views.result_api, name='list_result'),
]