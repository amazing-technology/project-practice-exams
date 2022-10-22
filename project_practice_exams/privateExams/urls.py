from django.urls import path
from privateExams.views import CreateExamEndPoint,getQuestions


urlpatterns = [
    path('',CreateExamEndPoint.as_view(),name="exam"),
    path('quest', getQuestions.as_view(), name="quest"),
]
