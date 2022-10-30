from privateExams.models import Exam, Question,Answer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from privateExams.serializer import ExamSerializer,QuestionSerializer,AnswerSerializer


# Create your views here.


class CreateExamEndPoint(APIView):

    def get(self,request,format=None):
        data = Exam.objects.all()
        serializer = ExamSerializer(data,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request,format=None):

        serializer = ExamSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class getQuestions(APIView):

    def get(self,request, format=None):
        data = Question.objects.all()
        serializer = QuestionSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class answerView(APIView):

    def get(self,request,format=None):
        data = Answer.objects.all()
        serializer = AnswerSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


