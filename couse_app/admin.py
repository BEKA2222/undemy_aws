from django.contrib import admin
from .models import (
    UserProfile, Category, Course, Lessons, Assignment,
    WhoPassedTest, Exam, Questions, Variants, Certificates
)

class VariantsInline(admin.TabularInline):
    model = Variants
    extra = 1

class QuestionsAdmin(admin.ModelAdmin):
    inlines = [VariantsInline]


admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lessons)
admin.site.register(Assignment)
admin.site.register(WhoPassedTest)
admin.site.register(Exam)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Certificates)