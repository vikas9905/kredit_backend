from dataclasses import fields
from rest_framework import serializers
from .models import User,PaymentDetails,PaymentProvider,UserPaymentOptions,Question,QuestionTag,Answer,OrderDetails,Options,Quizs,QuizTaken,CreditDebit,SavedAnswers,DeleteUserRequest
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
class PaymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=PaymentDetails
        fields='__all__'
class PaymentProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model=PaymentProvider
        fields='__all__'
class UserPaymentOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserPaymentOptions
        fields='__all__'
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields='__all__'
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderDetails
        fields='__all__'
class QuestionTagSerializer(serializers.ModelSerializer):
    class Meta:
        model=QuestionTag
        fields='__all__'
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields='__all__'
class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Options
        fields='__all__'
class QuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = []
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizs
        fields = '__all__'
class QuizTakenSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizTaken
        fields = '__all__'

class CreditDebitSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditDebit
        fields = '__all__'
class SavedAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedAnswers
        fields = '__all__'
class DeleteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeleteUserRequest
        fields = '__all__'


