from rest_framework import viewsets
from .serializers import FormSerializer,  QuestionSerializer, AnswerSerializer, ApplicantSerializer, ApplicantAnswerSerializer, ApplicantFormSerializer, UserSerializer
from .models import Form, Question, Answer, Applicant, ApplicantForm, ApplicantAnswer, User
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated


class FormViewSet(viewsets.ModelViewSet):
   
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    


class QuestionViewSet(viewsets.ModelViewSet):
    
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

        

class AnswerViewSet(viewsets.ModelViewSet):
    
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
    


class ApplicantViewSet(viewsets.ModelViewSet):
    
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    permission_classes = [IsAdminUser]
    


class ApplicantAnswerViewSet(viewsets.ModelViewSet):
    queryset = ApplicantAnswer.objects.all()
    serializer_class = ApplicantAnswerSerializer
    permission_classes = [IsAuthenticated]
    
    
    
class ApplicantFormViewSet(viewsets.ModelViewSet):
    queryset = ApplicantForm.objects.all()
    serializer_class = ApplicantFormSerializer
    permission_classes = [IsAuthenticated]
   
   
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
 

    