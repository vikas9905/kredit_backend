from dataclasses import field, fields
from distutils.command.upload import upload
from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50,primary_key=True)
    total_coins = models.IntegerField()

class PaymentProvider(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10)

class UserPaymentOptions(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    payment_num = models.IntegerField()
    provider = models.ForeignKey(PaymentProvider,on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)

class OrderDetails(models.Model):
    order_id = models.CharField(max_length=100,primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    ammount_requested = models.IntegerField(default=0)
    used_coin = models.IntegerField(default=0)
    payment_option = models.ForeignKey(UserPaymentOptions,on_delete=models.CASCADE)

class PaymentDetails(models.Model):
    order_id = models.ForeignKey(OrderDetails,on_delete=models.CASCADE)
    ammount_paid = models.IntegerField()
    payment_status= models.BooleanField(default=False)
    for_coins = models.IntegerField()
    comments = models.CharField(max_length=200)

class Quizs(models.Model):
    level = models.IntegerField()
    num_of_ques = models.IntegerField()
    total_coins = models.IntegerField()
    users_won = models.IntegerField(default=0,null=True,blank=True)

class QuestionTag(models.Model):
    tag_name = models.CharField(max_length=100)

class Question(models.Model):
    tag_id = models.ForeignKey(QuestionTag,on_delete=models.CASCADE)
    question = models.CharField(max_length=300)
    level = models.IntegerField()
    coins = models.IntegerField()
    quiz_id = models.ForeignKey(Quizs,on_delete=models.CASCADE,blank=True,null=True,default=None)
    question_type = models.CharField(max_length=10,default='text',blank=True,null=True)
    url = models.FileField(upload_to='questions/',null=True,blank=True)

class Options(models.Model):
    qid = models.ForeignKey(Question,on_delete=models.CASCADE)
    optionNum = models.CharField(max_length=10)
    optionValue = models.CharField(max_length=200)

class Answer(models.Model):
    qid = models.ForeignKey(Question,on_delete=models.CASCADE)
    option_id = models.ForeignKey(Options,on_delete=models.CASCADE)

class QuizTaken(models.Model):
    quiz_id = models.ForeignKey(Quizs,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True,default=None,blank=True)
    correct_ans = models.IntegerField()
    incorrect_ans = models.IntegerField()
    earned_coins = models.IntegerField()
