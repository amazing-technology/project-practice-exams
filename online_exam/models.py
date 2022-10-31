

# from django.db import models
# from django.contrib.auth.models import User
# from datetime import datetime

# # Create your models here.


# # def upload_image(instance, filename):
# #     return "%s/%s" % (instance.user, filename)
# EXAM_STATUSES=(
#         ('OPEN','Open'),
#         ('CLOSE','Close'),
# )

# class Exams(models.Model):
#     createdby = models.ForeignKey(User, limit_choices_to={'groups__name': "Professor"}, on_delete=models.CASCADE)
#     exam_name = models.CharField(max_length=50)
#     no_of_ques = models.CharField(max_length=20)
#     total_marks = models.CharField(max_length=20)
#     time_duration = models.DurationField(default='00:00:00')
#     start_time = models.DateTimeField(default=datetime.now())
#     end_time = models.DateTimeField(default=datetime.now())
#     timestamps = models.DateTimeField(auto_now_add=True, null=False)
#     exam_status =models.BooleanField(max_length=25,choices=EXAM_STATUSES,default=EXAM_STATUSES[0][0])


#     def __str__(self):
#         return str(self.exam_name)

# class Marks(models.Model):
#     exam_name = models.ForeignKey(Exams, on_delete=models.PROTECT, null=True)
#     user = models.ForeignKey(User, limit_choices_to={'groups__name': "Student"}, on_delete=models.CASCADE, null=True)
#     no_ques_attempt = models.Count
#     no_ques_unattempt = models.Count
#     no_ques_right = models.Count
#     no_ques_wrong = models.Count
#     total_mark = models.Count
#     DESTION = ({'pass', 'PASS'}, {'fail', 'FAIL'})
#     decision = models.CharField(choices = DESTION)
#     timestamps = models.DateTimeField(auto_now_add=True, null=False)
#     status =models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.exam_name}, {self.user}, {self.decision}"


# questionCategory = [
#      {'I.beginners', 'I.BEGINNERS'},
#     ('QUESTION TYPE_BEGINNERS',(
#             ('I.1. traffic light', 'I.1. TRAFFIC LIGHT '),
#             ('I.2. ubwikorezi', ' I.2. UBWIKOREZI'),
#             ('I.3. ibyerekeyekugenda mu muhanda', ' I.3. IBYEREKEYE KUGENDA MU MUHANDA'),    

#         )),

#     ('QUESTION TYPE_INTERMEDIATE',(
#             ('II.1. traffic light', 'II.1. TRAFFIC LIGHT '),
#             ('II.2. ubwikorezi', ' II.2. UBWIKOREZI'),
#             ('II.3. ibyerekeyekugenda mu muhanda', ' II.3. IBYEREKEYE KUGENDA MU MUHANDA'),    

#         )),
    
#     ('QUESTION TYPE_ADVANCED',(
#             ('III.1. traffic light', 'III.1. TRAFFIC LIGHT '),
#             ('III.2. ubwikorezi', ' III.2. UBWIKOREZI'),
#             ('III.3. ibyerekeyekugenda mu muhanda', ' III.3. IBYEREKEYE KUGENDA MU MUHANDA'),    

#         )),
  
# ]

# class Question(models.Model):
#     qno = models.AutoField(primary_key=True)
#     createdby  = models.ForeignKey('User', limit_choices_to={'groups__name': "Professor"}, on_delete=models.PROTECT, null=True)
#     questionCategory = models.CharField(choices=questionCategory, max_length=255, blank=False,null= True)
#     exam_name = models.ForeignKey(Exams, on_delete=models.CASCADE)
#     marks = models.PositiveIntegerField(default=0)
#     question = models.TextField(max_length=500)
#     optionA = models.CharField(max_length=100)
#     optionB = models.CharField(max_length=100)
#     optionC = models.CharField(max_length=100)
#     optionD = models.CharField(max_length=100)
#     choose = (('A', 'option1'), ('B', 'option2'), ('C', 'option3'), ('D', 'option4'))
#     answer = models.CharField(max_length=1, choices=choose)
#     timestamps = models.DateTimeField(auto_now_add=True, null=False)
#     status =models.BooleanField(default=False)



#     def __str__(self):
#         return f'Question No.{self.qno}: {self.question} \t\t Options: \nA. {self.optionA} \nB.{self.optionB} \nC.{self.optionC} \nD.{self.optionD} '


from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils.timezone import now




# Create your models here.

COURSE_TYPE = [
    ("FREE","FREE"),
    ("PAID","PAID"),
]

class Course(models.Model):
    title = models.CharField(max_length=100)
    file_attachment = models.FileField(upload_to='course_Attachment/pdfs/',  null=True, blank=True)
    description = models.TextField()
    thumbnail_url = models.CharField(max_length=100)
    course_type = models.CharField(max_length=4,choices=COURSE_TYPE, default="FREE")
    course_length = models.CharField(max_length=20)
    course_slug = models.SlugField(default="-")
    course_price = models.IntegerField(default=0)

    # def __str__(self):
    #     return f"{self.course_type} - {self.title}."


class StudentComment(models.Model):
    comment = models.TextField()
    timestamp = models.DateTimeField(default=now)





