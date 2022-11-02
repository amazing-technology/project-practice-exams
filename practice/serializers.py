
from rest_framework import serializers
from .models import *
from online_exam.models import ExamSubscription, PaymentProcess



class ExamsSerializer(serializers.ModelSerializer):
    
    createdby = serializers.StringRelatedField()

    class Meta:
        model = Exams
        fields = '__all__'
       


class MarksSerializer(serializers.ModelSerializer):
     exam_name = serializers.StringRelatedField()
     registration_id = serializers.StringRelatedField()
     model = Marks
     fields = '__all__'
   
class QuestionSerializer(serializers.ModelSerializer):
    createdby = serializers.StringRelatedField() 

    class Meta:
        model = Question
        fields = '__all__'

class  SetSerializer(serializers.Serializer):
     exam_id = serializers.StringRelatedField()
     
     model = Marks
     fields = ['id', 'set_no', ' ques', 'no_of_question', 'no_ques_unattempt','exam_id']

class AnswersSerializer(serializers.Serializer):
    exam_name = serializers.StringRelatedField()
    question_id = serializers.StringRelatedField()
    class Meta:
        model = Answers
        fields = ['id','question_id','aded_by','answer','timestamps','status']

class MatchTheColumnsSerializer(serializers.ModelSerializer):
    question_id = serializers.StringRelatedField()
    class Meta:
        model = MatchTheColumns
        fields = ['id','question_id','question','answer']


class Quastion_dbSerializer(serializers.Serializer):
    
    class Meta:
        model = Quastion_db
        fields = ['questionCategory','questionName','optionA','optionB','optionC','optionD','optionE','optionF','answer']

class ExamSubscriptionSerializer(serializers.Serializer):
    examPractice = serializers.StringRelatedField()
    candidate = serializers.StringRelatedField()
    class Meta:
        model = ExamSubscription
        fields = ['candidate',' examPractice','DateStamp','progress','payment_id','order_id']
class PaymentProcessSerializer(serializers.Serializer):
    examPractice = serializers.StringRelatedField()
    candidate = serializers.StringRelatedField()
    class Meta:
        model = PaymentProcess
        fields = ['examPractice','candidate','order_id','payment_status','datestamp']