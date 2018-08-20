from django.contrib import admin
from .models import Question, Choice
# Register your models here.
class ChoiceInline(admin.StackedInline): # TabularInline
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_pulished_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
# class ChoiceAdmin(admin.ModelAdmin):
#     fields = ['question', 'choice_text', 'votes']

admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice, ChoiceAdmin)