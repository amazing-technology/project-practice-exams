import email
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse

# rest framework imports
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

# local imports
from .serializers import *
from .models import *

# Create your views here.

# index page api
@api_view(["GET"])
@permission_classes((AllowAny,))
def index(request):
    """
    Index API
    """
    return Response({"message": "Welcome to assessment API service"})


#######################################
# User APIs below
#######################################

# register new user to exam portal

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def signup_api(request):
    """
    Register new user to the exam portal
    """
    fullName = request.data.get("fullName", None)
    userType = request.data.get("userType",None)
    phone = request.data.get("phone", None)
    username = request.data.get("username", None)
    email = request.data.get("email",None)
    password = request.data.get("password", None)
    address = request.data.get("address", None)
    
   

    
    if Users.objects.filter(username=username).exists():
        return Response({'error': 'username already exist'}, status=HTTP_400_BAD_REQUEST)
    
    if Users.objects.filter(email = email).exists():
        return Response({'error': 'email already exist'}, status=HTTP_400_BAD_REQUEST)
    
    if Users.objects.filter(phone = phone).exists():
        return Response({'error': 'phone already exist'}, status=HTTP_400_BAD_REQUEST)


    if username and password:
        user = Users(username=username)
        user.set_password(raw_password=password)
        user.save()
        return Response({'success': 'User has been created'}, status=HTTP_201_CREATED)
    return Response({'error': 'Please provide username and password'}, status=HTTP_400_BAD_REQUEST)


# login existing user to exam portal
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login_api(request):
    """
    Login the user to exam portal
    """
    username = request.data.get("username")
    password = request.data.get("password")

    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)

    if not user:
        return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=HTTP_200_OK)


# start test api
@api_view(['GET', 'POST'])
# @permission_classes((IsAuthenticated,))
@permission_classes((AllowAny,))
def Question_list_api(request, format=None):
    """
    Start the new exam giving list of all question papers
    """
    if request.method == 'GET':
        question = Question.objects.all()
        serializer = QuestionSerializer(question, many=True)
        return Response (serializer.data)
    
    elif request.method == 'POST':
        serializer = QuestionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def Question_api_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code questions.
    """
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = QuestionSerializer(dtata = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
# @permission_classes((IsAuthenticated,))
@permission_classes((AllowAny,))
def Exam_list_api(request, format=None):
    if request.method == 'GET':
        createExam = Exams.objects.all()
        serializer = ExamsSerializer(createExam, many = True)
        return Response(serializer.data)
    
    
    elif  request.method == 'POST':

        serializer = ExamsSerializer(dtata = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def Exam_api_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code Exam.
    """
    try:
        exam = Exams.objects.get(pk=pk)
    except Exams.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ExamsSerializer(exam)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ExamsSerializer(exam, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        exam.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        






   
    
# # calculate test result
# @api_view(["POST"])
# @permission_classes((IsAuthenticated,))
# def store_result_api(request):
#     """
#     Create score card based on options selected by users for each questions
#     strongly_agree = 2
#     agree = 1
#     neutral = 0
#     disagree = -1
#     strongly_disagree = -2
#     """
#     answer_sheet = request.data
#     marks = {}
#     for item in answer_sheet:
#         que_type = item['que_type']
#         ans = item['selected_option']
#         if que_type not in marks.keys():
#             marks[que_type] = 0
#             if ans == 'strongly_agree':
#                 marks[que_type] += 2
#             if ans == 'agree':
#                 marks[que_type] += 1
#             if ans == 'neutral':
#                 marks[que_type] += 0
#             if ans == 'disagree':
#                 marks[que_type] += -1
#             if ans == 'strongly_disagree':
#                 marks[que_type] += -2
#         else:
#             if ans == 'strongly_agree':
#                 marks[que_type] += 2
#             if ans == 'agree':
#                 marks[que_type] += 1
#             if ans == 'neutral':
#                 marks[que_type] += 0
#             if ans == 'disagree':
#                 marks[que_type] += -1
#             if ans == 'strongly_disagree':
#                 marks[que_type] += -2

#     total = sum([x[1] for x in marks.items()])
#     score_card = {'user': request.user.username, 'marks': marks, 'total': total, 'top_qualities': []}

#     if Result.objects.filter(user=request.user).exists():
#         result = Result.objects.get(user=request.user)
#         result.score = total
#         result.save()
#         response = {"success": "Exam submitted successfully", "score_card": score_card}
#         return Response(response, status=HTTP_200_OK)
#     else:
#         result = Result.objects.create(score=total, user=request.user)
#         result.save()
#         response = {"success": "Exam submitted successfully", "score_card": score_card},
#         return Response(response, status=HTTP_200_OK)


#######################################
# Admin only APIs below
#######################################

# # upload questions csv file
# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((IsAdminUser,))
# def upload_question_api(request):
#     """
#     Uploads CSV file having 3 columns- sr/no, questions, questions type
#     """
#     csv_file = request.FILES['questions']
#     # check whether file is csv or not
#     if not csv_file.name.endswith('.csv'):
#         return Response({"error": "please upload valid csv file"}, status=HTTP_400_BAD_REQUEST)

#     # if file is too large, return
#     if csv_file.multiple_chunks():
#         return Response({"error": "Uploaded file is too big"}, status=HTTP_400_BAD_REQUEST)

#     file = csv_file.read().decode('UTF-8')
#     lines = file.split("\n")[1:-1]
#     for row in lines:
#         line = row.split(',')
#         question = Question.objects.create(question=line[1], que_type=line[2])
#         question.save()
#     return Response({"success": "Questions uploaded successfully"}, status=HTTP_200_OK)


# @csrf_exempt
# @api_view(["GET", "PUT", "DELETE"])
# # @permission_classes((IsAdminUser,))
# def questions_api(request, que_id=None):
#     """
#     Let admin view all questions
#     """
#     # get all questions
#     if request.method == 'GET':
#         ques = Question.objects.all()
#         ser = QuestionSerializer(ques, many=True)
#         data = {'questions': ser.data}
#         return Response(data, status=HTTP_200_OK)

#     # get one question object by id
#     try:
#         question = Question.objects.get(pk=que_id)
#     except Question.DoesNotExist:
#         return HttpResponse(status=404)

#     # update given question
#     if request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = QuestionSerializer(question, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'success': 'Question updated successfully'}, status=HTTP_200_OK)
#         return Response({'error': serializer.errors}, status=HTTP_400_BAD_REQUEST)

#     # delete given question
#     if request.method == 'DELETE':
#         question.delete()
#         return Response({"success": "Question deleted successfully"}, status=HTTP_204_NO_CONTENT)


# # get result of all users
# @api_view(["GET"])
# @permission_classes((IsAdminUser,))
# def result_api(request):
#     """
#     Let admin view all users result
#     """
#     try:
#         results = Result.objects.all()
#     except Result.DoesNotExist:
#         return HttpResponse(status=404)

#     # get all questions
#     if request.method == 'GET':
#         ser = ResultSerializer(results, many=True)
#         data = {'result': ser.data}
#         return Response(data, status=HTTP_200_OK)
