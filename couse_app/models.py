from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    ROLE_USERS = (
        ('student', 'student'),
        ('teacher', 'teacher'),
    )
    role = models.CharField(max_length=10, choices=ROLE_USERS, default='student')
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username


class Category(models.Model):
    category_name = models.CharField(max_length=32)

    def __str__(self):
        return self.category_name


class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=32)
    description = models.TextField(null=True , blank=True)
    LEVEL_CHOICES = (
        ('Начальный', 'Начальный'),
        ('Средний', 'Средний'),
        ('Продвинутый', 'Продвинутый'),
    )
    level = models.CharField(max_length=15, choices=LEVEL_CHOICES)
    price = models.DecimalField(max_digits=8 , decimal_places=2, null=True, blank=True)
    teacher = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_ad = models.DateField(auto_now_add=True)
    updated_ad = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.category} - {self.course_name}'


class Lessons(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons_course')
    title = models.CharField(max_length=32)
    video = models.FileField(upload_to='videos_lessons', null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.course} - {self.title}'


class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    description = models.TextField(null=True, blank=True)
    due_data = models.DateTimeField()

    def __str__(self):
        return f'{self.course} - {self.title}'


class WhoPassedTest(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    solution_file = models.FileField(null=True, blank=True)
    solution_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.student} - {self.assignment}'


class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    duration = models.DateTimeField()

    def __str__(self):
        return f'{self.course} - {self.title}'


class Questions(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_title = models.TextField()

    def __str__(self):
        return f'{self.exam} - {self.question_title}'


class Variants(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='variants_question')
    variant = models.CharField(max_length=135)

    def __str__(self):
        return f'{self.question} - {self.variant}'


class Certificates(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    certificate_file = models.FileField()
    issued_ad = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.course} - {self.student}'