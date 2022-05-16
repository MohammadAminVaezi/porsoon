from django.urls import path
from rest_framework.routers import DefaultRouter
from sin_jim.views import FormViewSet, QuestionViewSet, AnswerViewSet, ApplicantViewSet, ApplicantAnswerViewSet, ApplicantFormViewSet, UserViewSet


router = DefaultRouter()
router.register(r'form', FormViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'answer', AnswerViewSet)
router.register(r'applicant', ApplicantViewSet)
router.register(r'applicantanswer', ApplicantAnswerViewSet)
router.register(r'applicantform', ApplicantFormViewSet)
router.register(r'user',  UserViewSet)

urlpatterns = [
    
] + router.urls