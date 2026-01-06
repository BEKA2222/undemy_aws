from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsTeacher, IsStudent, IsTeacherOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .pagination import CoursePagination
from .models import (


    UserProfile, Category, Course, Lessons, Assignment,
    WhoPassedTest, Exam, Questions, Variants, Certificates
)
from .serializers import (
    UserProfileSerializer, CategorySerializer, CourseListSerializer, CourseDetailSerializer,
    LessonsSerializer, AssignmentSerializer, WhoPassedTestSerializer,
    ExamListSerializer,ExamDetailSerializer, QuestionsListSerializer, QuestionsDetailSerializer, VariantsSerializer, CertificatesSerializer,
    ExamDetailSerializer
)



class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CourseListViewSet(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'price']
    search_fields = ['course_name']
    ordering_fields = ['price', 'created_ad']
    permission_classes = [IsTeacherOrReadOnly]
    pagination_class = CoursePagination

class CourseDetailViewSet(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    permission_classes = [IsTeacherOrReadOnly]

class LessonsViewSet(viewsets.ModelViewSet):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer
    permission_classes = [IsTeacherOrReadOnly]

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsTeacherOrReadOnly]

class WhoPassedTestViewSet(viewsets.ModelViewSet):
    queryset = WhoPassedTest.objects.all()
    serializer_class = WhoPassedTestSerializer
    permission_classes = [IsTeacher]

class ExamListViewSet(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamListSerializer

class ExamDetailViewSet(generics.RetrieveAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamDetailSerializer


class QuestionsListViewSet(generics.ListAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsListSerializer


class QuestionsDetailViewSet(generics.RetrieveAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsDetailSerializer


class VariantsViewSet(viewsets.ModelViewSet):
    queryset = Variants.objects.all()
    serializer_class = VariantsSerializer

class CertificatesViewSet(viewsets.ModelViewSet):
    queryset = Certificates.objects.all()
    serializer_class = CertificatesSerializer