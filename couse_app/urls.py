from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import (
    UserProfileViewSet, CategoryViewSet, CourseListViewSet, CourseDetailViewSet, LessonsViewSet,
    AssignmentViewSet, WhoPassedTestViewSet, ExamListViewSet, ExamDetailViewSet,
    QuestionsListViewSet, QuestionsDetailViewSet, VariantsViewSet, CertificatesViewSet
)

router = SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='users')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'lessons', LessonsViewSet, basename='lessons')
router.register(r'assignments', AssignmentViewSet, basename='assignments')
router.register(r'whopassedtest', WhoPassedTestViewSet, basename='whopassedtest')
router.register(r'variants', VariantsViewSet, basename='variants')
router.register(r'certificates', CertificatesViewSet, basename='certificates')

urlpatterns = [
    path('', include(router.urls)),
    path('course/', CourseListViewSet.as_view(), name='course-list'),
    path('course/<int:pk>/', CourseDetailViewSet.as_view(), name='course-detail'),
    path('question/', QuestionsListViewSet.as_view(), name='question-list'),
    path('question/<int:pk>/', QuestionsDetailViewSet.as_view(), name='question-detail'),
    path('exam/', ExamListViewSet.as_view(), name='exam-list'),
    path('exam/<int:pk>/', ExamDetailViewSet.as_view(), name='exam-detail'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]