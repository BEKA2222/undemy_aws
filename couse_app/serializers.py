from rest_framework import serializers
from .models import (
    UserProfile, Category, Course, Lessons, Assignment,
    WhoPassedTest, Exam, Questions, Variants, Certificates
)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class LessonsSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = ['id', 'title', 'video', 'video_url', 'content']


class CourseListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Course
        fields = ['id', 'category', 'course_name', 'price']


class CourseDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    teacher =UserProfileSerializer()
    lessons_course = LessonsSimpleSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['id', 'category', 'course_name', 'teacher', 'level', 'description', 'created_ad',
                  'updated_ad', 'lessons_course']

class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = '__all__'

class AssignmentSerializer(serializers.ModelSerializer):
    course = CourseListSerializer()
    class Meta:
        model = Assignment
        fields = ['id', 'title', 'description', 'due_data', 'course']

class WhoPassedTestSerializer(serializers.ModelSerializer):
    student = UserProfileSerializer()
    assignment = AssignmentSerializer()
    class Meta:
        model = WhoPassedTest
        fields = ['id', 'student', 'assignment', 'solution_file', 'solution_url']

class ExamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['title']


class ExamDetailSerializer(serializers.ModelSerializer):
    course = CourseListSerializer()
    class Meta:
        model = Exam
        fields = ['id', 'title', 'course', 'duration', ]


class QuestionsListSerializer(serializers.ModelSerializer):
    exam = ExamListSerializer()
    class Meta:
        model = Questions
        fields = ['id', 'question_title', 'exam']


class VariantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variants
        fields = ['id', 'variant']


class QuestionsDetailSerializer(serializers.ModelSerializer):
    exam = ExamDetailSerializer()
    variants_question = VariantsSerializer(read_only=True, many=True)
    class Meta:
        model = Questions
        fields = ['id', 'question_title', 'exam', 'variants_question']


class CertificatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificates
        fields = '__all__'