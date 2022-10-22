from rest_framework import serializers
from privateExams.models import Exam, Question, Answer




class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['order', 'content']
        # fields = '__all__'


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
            Question.objects.create(exam=exam, **question)
        return exam
