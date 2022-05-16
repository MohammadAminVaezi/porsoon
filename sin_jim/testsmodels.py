from django.test import TestCase
from .models import Applicant, Form, Question, Answer


class TestForm(TestCase):
    def setUp(self):
        Form.objects.create(title='Skill test', description='backend skill test', owner='pishdad')

    def Test__str__(self):
        form = Form.objects.get(title='Skill test')
        self.assertEqual(form.__str__(), 'backend skill test')



class TestQuestion(TestCase):
    def setUp(self):
        q1 = Form.objects.create(title='Skill test11', description='frontend skill test', owner='makeen')
        question = Question.objects.create(order='1', text='what is your name?', is_required='True')
        Question.Form.add(q1)
        question.save()

    def test__str__(self):
        question = Question.objects.get(order= 1)
        self.assertEqual(question.__str__(), 1)




class TestAnswer(TestCase):
    def setUp(self):
        a1 = Question.objects.create(order= 1, text='what is your name?', is_required='True')
        answer = Answer.objects.create(order= 1, question='how old are you?', text= 30)
        Question.Answer.add(a1)
        answer.save()

    def test__str__(self):
        answer = Answer.objects.get(order='1')
        self.assertEqual(answer.__str__(), '1') 




class TestApplicant(TestCase):
    def setUp(self):
        Applicant.objects.create(first_name='mmd', last_name='ahmadi', age='23', phone='09908743112', email='mmd@gmail.com')

    def Test__str__(self):
        applicant = Applicant.objects.get(last_name='ahmadi')
        self.assertEqual(applicant.__str__(), 'ahmadi')