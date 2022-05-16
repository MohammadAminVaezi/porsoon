from rest_framework import serializers
from .models import Form, Question, Answer, Applicant, ApplicantForm, ApplicantAnswer, User


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ('title','description','owner')


        def create(self, validated_data):
            user =  self.context['user']
            validated_data["owner"] = user
            instance = super().create(validated_data)      
            return instance



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('__all__')



class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('__all__')



class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ('__all__')
        


class ApplicantFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantForm
        fields = ('__all__')
        



class ApplicantAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantAnswer
        fields = ('__all__')
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password')
   