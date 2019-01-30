from django.contrib import admin
from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']


# class ChoiceAdmin(admin.ModelAdmin):
# fields = ['choice_text']

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question_text', 'pub_date',)
    list_filter = ['pub_date']
    search_fields = ['question_text']

    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)
