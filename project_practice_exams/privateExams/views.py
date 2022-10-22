from django.shortcuts import render
from privateExams.models import Exam, Question
from privateExams.serializer import ExamSerializer,QuestionSerializer
from privateExams.models import Exam
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

# Create your views here.


class CreateExamEndPoint(APIView):
    
    
    def get(self,request,format=None):
        data = Exam.objects.all()
        serializer = ExamSerializer(data, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request,format=None):

        serialiser = ExamSerializer(data=request.data)
        if serialiser.is_valid():           
            serialiser.save()
            return Response(serialiser.data,status=status.HTTP_201_CREATED)
        return Response(serialiser.errors,status=status.HTTP_400_BAD_REQUEST)

class getQuestions(APIView):

    def get(self, request, format=None):
        data = Question.objects.all()
        serializer = QuestionSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



