from django.contrib import admin
from quiz.models import Course,Question,Result
# Register your models here.

class course(admin.ModelAdmin):
    list_display = ('course_name','question_number','total_marks')

admin.site.register(Course,course)

class questions(admin.ModelAdmin):
    list_display = ('course','marks','question','option1','option2','option3','option4','cat','answer')

admin.site.register(Question,questions)

class result(admin.ModelAdmin):
    list_display = ('student','exam','marks','date')

admin.site.register(Result,result)

