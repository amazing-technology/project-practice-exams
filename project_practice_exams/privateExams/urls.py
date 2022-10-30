from django.urls import path
from privateExams.views import CreateExamEndPoint,getQuestions,answerView


urlpatterns = [
    path('',CreateExamEndPoint.as_view(),name="exam"),
    path('quest', getQuestions.as_view(), name="quest"),
    path('ans', answerView.as_view(), name="ans"),
]