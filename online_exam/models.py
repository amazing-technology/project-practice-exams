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

    def __str__(self):
        return f"{self.course_type} - {self.title}."


class StudentComment(models.Model):
    comment = models.TextField()
    timestamp = models.DateTimeField(default=now)





