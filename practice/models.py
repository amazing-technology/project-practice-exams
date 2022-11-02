from email.policy import default
from enum import unique
import django
from django.conf import UserSettingsHolder
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.timezone import now
from django.utils import timezone

# Create your models here.



EXAM_STATUSES=(
        ('OPEN','Open'),
        ('CLOSE','Close'),
)
USERTYPE=(
        ('CANDIDATE','candidate'),
        ('SCHOOL TEACHER','School Teacher'),
)

class MyAccountManager(BaseUserManager):
    def create_user(self,phone, fullName,email,password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not fullName:
            raise ValueError('Users must have a username')
        if not phone:
            raise ValueError('you must provide your phone')

        user = self.model(
            email=self.normalize_email(email),
            username=fullName,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,fullName, email, password):
        user = self.create_user(
            fullName = fullName,
            email=self.normalize_email(email),
            password=password,
         
            
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class Users(AbstractBaseUser):
    fullName = models.CharField(max_length=20)
    userType = models.CharField(max_length=255,choices = USERTYPE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$',
                                 message="Phone number must be entered in the define format")
    phone = models.CharField(validators=[phone_regex], max_length=12)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=200, blank=True)
    date_joined             = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login              = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin                = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=True)
    is_staff                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullName']

    objects = MyAccountManager()


    def __str__(self):
        return str(self.fullName)
        # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

class Exams(models.Model):
    createdby = models.ForeignKey(Users, on_delete=models.CASCADE)
    exam_name = models.CharField(max_length=50)
    description = models.TextField(null="True", blank=True)
    start_time = models.DateTimeField(default=django.utils.timezone.now)
    end_time = models.DateTimeField(default=django.utils.timezone.now)
    no_of_ques = models.CharField(max_length=20)
    attempts_allowed = models.IntegerField(blank = True, null = True)
    pass_percentage = models.IntegerField(blank = True, null = True)   
    total_marks = models.CharField(max_length=20)
    time_duration = models.DurationField(default='00:00:00')
   
    created = models.DateTimeField(default = timezone.now)
    modified = models.DateTimeField(default = timezone.now)
    exam_status =models.BooleanField(default = False)


    def __str__(self):
        return f'{self.exam_name}'
        
class Candidates(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    exam_id =  models.ForeignKey(Exams, on_delete=models.CASCADE)
    attempt_no = models.IntegerField()
    registered = models.IntegerField(default = 0)
    view_answers  = models.IntegerField(default = 0)
    answered = models.IntegerField(default = 0)
    score = models.IntegerField(default=0)
    registered_time = models.DateTimeField(default = timezone.now)
    status =models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + "; " + str(self.user_id) + "; " + str(self.exam_id) + "; " + str(self.attempt_no) + "; " + str(self.registered) + "; " + str(self.view_answers) + "; " + str(self.answered) + "; " + str(self.registered_time)

class Marks(models.Model):
    exam_id = models.ForeignKey(Exams, on_delete=models.PROTECT, null=True)
    registration_id = models.ForeignKey(Candidates, on_delete = models.CASCADE, blank = False,null = True)
    no_ques_attempt = models.Count
    no_ques_unattempt = models.Count
    no_ques_right = models.Count
    no_ques_wrong = models.Count
    answer = models.TextField(null="True", blank=True)
    total_marks = models.Count
    DESTION = ({'pass', 'PASS'}, {'fail', 'FAIL'})
    decision = models.CharField(max_length=255,choices = DESTION)
    verify = models.IntegerField(default = 0)

    def __str__(self):  
        return str(self.id) + "; " + str(self.registration_id) + "; " + str(self.exam_id) + "; " + str(self.answer) + "; " + str(self.total_marks) + "; " + str(self.verify) 


questionCategory = [
    
    ('QUESTION TYPE_BEGINNERS',(
            ('I.1. traffic light', 'I.1. TRAFFIC LIGHT '),
            ('I.2. ubwikorezi', ' I.2. UBWIKOREZI'),
            ('I.3. ibyerekeyekugenda mu muhanda', ' I.3. IBYEREKEYE KUGENDA MU MUHANDA'),    

        )),

    ('QUESTION TYPE_INTERMEDIATE',(
            ('II.1. traffic light', 'II.1. TRAFFIC LIGHT '),
            ('II.2. ubwikorezi', ' II.2. UBWIKOREZI'),
            ('II.3. ibyerekeyekugenda mu muhanda', ' II.3. IBYEREKEYE KUGENDA MU MUHANDA'),    

        )),
    
    ('QUESTION TYPE_ADVANCED',(
            ('III.1. traffic light', 'III.1. TRAFFIC LIGHT '),
            ('III.2. ubwikorezi', ' III.2. UBWIKOREZI'),
            ('III.3. ibyerekeyekugenda mu muhanda', ' III.3. IBYEREKEYE KUGENDA MU MUHANDA'),    

        )),
  
]

class Question(models.Model):
    qno = models.AutoField(primary_key=True)
    createdby  = models.ForeignKey(Users, on_delete=models.PROTECT, null=True)
    questionCategory = models.CharField(choices=questionCategory, max_length=255, blank=False,null= True)
    exam_id = models.ForeignKey(Exams, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField(default=0)
    question = models.TextField(max_length=500, blank = True, null = True)
    optionA = models.CharField(max_length=100, blank = True, null = True)
    optionB = models.CharField(max_length=100, blank = True, null = True)
    optionC = models.CharField(max_length=100, blank = True, null = True)
    optionD = models.CharField(max_length=100, blank = True, null = True)
    optionE = models.CharField(max_length=100, blank = True, null = True)
    optionF = models.CharField(max_length=100, blank = True, null = True)
    choose = (('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'),('E', 'E'),('F', 'F'))
    answer = models.CharField(max_length=1, choices=choose)
    timestamps = models.DateTimeField(default=now)
    status =models.BooleanField(default=False)



    def __str__(self):
        return f'Question No.{self.qno}: {self.createdby} \t\t Options: \nA. {self.optionA} \nB.{self.optionB} \nC.{self.optionC} \nD.{self.optionD} \nE.{self.optionE} \nF.{self.optionF}'



class Set(models.Model):
    set_no = models.PositiveIntegerField(default=0)
    ques = models.ManyToManyField(Question)
    no_of_question = models.Count(Question.question)
    exam_id = models.ForeignKey(Exams, on_delete=models.CASCADE)

    def __str__(self):
        
        return f' Question practice Title :- {self.exam_id}, {self.set_no}\n'


class Answers(models.Model):
    question_id  = models.ForeignKey(Question, on_delete=models.CASCADE)
    aded_by = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    choose = (('A', 'B'), ('B', 'B'), ('C', 'C'), ('D', 'D'),('E','E'),('F','F'))
    answer = models.CharField(max_length=1, choices=choose, null="True", blank=True)
    timestamps = models.DateTimeField(default = timezone.now)
    status =models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + "; " + str(self.question_id) + "; " + str(self.answer)
class MatchTheColumns(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    question = models.TextField(null="True", blank=True)
    answer = models.TextField(null="True", blank=True)
    def __str__(self):
        return str(self.id) + "; " + str(self.question_id) + "; " + str(self.question) + "; " + str(self.answer)

class Quastion_db(models.Model):
     questionCategory = [
    
    ('QUESTION TYPE_BEGINNERS',(
            ('I.1. traffic light', 'I.1. TRAFFIC LIGHT '),
            ('I.2. ubwikorezi', ' I.2. UBWIKOREZI'),
            ('I.3. ibyerekeyekugenda mu muhanda', ' I.3. IBYEREKEYE KUGENDA MU MUHANDA'),    

        )),

    ('QUESTION TYPE_INTERMEDIATE',(
            ('II.1. traffic light', 'II.1. TRAFFIC LIGHT '),
            ('II.2. ubwikorezi', ' II.2. UBWIKOREZI'),
            ('II.3. ibyerekeyekugenda mu muhanda', ' II.3. IBYEREKEYE KUGENDA MU MUHANDA'),    

        )),
    
    ('QUESTION TYPE_ADVANCED',(
            ('III.1. traffic light', 'III.1. TRAFFIC LIGHT '),
            ('III.2. ubwikorezi', ' III.2. UBWIKOREZI'),
            ('III.3. ibyerekeyekugenda mu muhanda', ' III.3. IBYEREKEYE KUGENDA MU MUHANDA'),    

        )),
  
]
     questionCategory = models.CharField(choices=questionCategory, max_length=255, blank=False,null= True)
     questionName = models.TextField(max_length=500)
     optionA = models.CharField(max_length=100, blank = True, null = True)
     optionB = models.CharField(max_length=100, blank = True, null = True)
     optionC = models.CharField(max_length=100, blank = True, null = True)
     optionD = models.CharField(max_length=100, blank = True, null = True)
     optionE = models.CharField(max_length=100, blank = True, null = True)
     optionF = models.CharField(max_length=100, blank = True, null = True)
     choose = (('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'),('E', 'E'),('F', 'F'))
     answer = models.CharField(max_length=1, choices=choose)
    