from django.db import models

# Create your models here.


class Exam(models.Model):

    title = models.CharField(null=False, blank=False, max_length=30, primary_key=True)
    starting_time = models.DateTimeField(null=False)
    finishing_time = models.DateTimeField(null=False)

    def __str__(self):
        return self.title
        


class Question(models.Model):

    exam = models.ForeignKey(Exam, related_name='questions', on_delete=models.CASCADE)
    content = models.CharField(null=True, max_length=50)
    order = models.IntegerField()

    class Meta:
        unique_together = ['order', 'content']
        ordering = ['order']
    
    def __str__(self):
        return '%d: %s' % (self.order, self.content)

class Answer(models.Model):

    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer_content = models.CharField(null=False, max_length=50)
    answer_flag = models.BooleanField(default=False)
    order = models.CharField(max_length=1)

    class Meta:
        unique_together = ['order', 'answer_content']
        ordering = ['order']

    def __str__(self):
        return '%c: %s' % (self.order, self.answer_content)
