from rest_framework import serializers
from privateExams.models import Exam, Question, Answer


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['answer_content','answer_flag','order']

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    class Meta:
        model = Question
        fields = ['order', 'content','answers']


class ExamSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    
    class Meta:
        model = Exam
        fields = ['title', 'starting_time',
                  'finishing_time', 'questions']

    def create(self, validated_data):


        all_questions = validated_data.pop('questions')
        exam = Exam.objects.create(**validated_data)

        for question in all_questions:
            
            all_answers = question.pop('answers')
            question_instance = Question.objects.create(exam=exam, **question)

            for answer in all_answers:
                Answer.objects.create(question=question_instance, **answer)

        return exam