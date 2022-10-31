from django.contrib import admin
from .models import *
from online_exam.models import Course, StudentComment
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Exams)
admin.site.register(Marks)
admin.site.register(Question)
admin.site.register(Set)
admin.site.register(Answers)
admin.site.register(Candidates)
admin.site.register(Users)
admin.site.register(Course)
admin.site.register(StudentComment)
# admin.site.register( Quastion_db)

@admin.register(Quastion_db)
class Quastion_db(ImportExportModelAdmin):
    list_display = ('questionName', 'optionA', 'optionB', 'optionC', 'optionD', 'answer')