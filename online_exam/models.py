

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from practice.models import Exams, Users

# Create your models here.


class ExamSubscription(models.Model):
    candidate = models.ForeignKey(Users, on_delete=models.CASCADE)
    examPractice = models.ForeignKey(Exams,max_length=255, on_delete=models.CASCADE, blank = True, null = True)
    DateStamp = models.DateTimeField(default=now)
    progress = models.CharField(default="0 %", max_length=10)
    payment_id = models.CharField(max_length=50, default="-")
    order_id = models.CharField(max_length=50, default="-")

    def __str__(self):
        return f"{self.candidate.username} ==== {self.examPractice}"

class PaymentProcess(models.Model):
    examPractice = models.ForeignKey(Exams, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Users, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=50, default="-")
    payment_status = models.BooleanField(default=False)
    datestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.examPractice} - {self.order_id} - {self.payment_status}"