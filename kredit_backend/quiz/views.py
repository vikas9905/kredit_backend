from email.policy import HTTP
from functools import partial
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import json
from .models import User,UserPaymentOptions,PaymentDetails,PaymentProvider,OrderDetails,Question,QuestionTag,Options,Answer,QuizTaken,Quizs
from .serializer import UserSerializer,UserPaymentOptionsSerializer,PaymentDetailsSerializer,PaymentProviderSerializer,OrderSerializer,QuestionSerializer,QuestionTagSerializer,OptionSerializer,AnswerSerializer,QuizSerializer,QuizTakenSerializer
from django.http import JsonResponse
class Users(APIView):
    def post(self,request,format=None):
        data=request.data
        print(data)
        serailizer=serializers.SellerSerializer(data=data)
        if serailizer.is_valid():
            serailizer.save()
            return Response(status.HTTP_200_OK)
        return Response({status:status.HTTP_400_BAD_REQUEST,msg:"Failed"})
    
    def get(self,request,id,format=None):
        if id==None:
            return Response({"status":'404',"data":"Record Not Found"})

        try:
            obj=User.objects.get(user_id=id)
            serializer=UserSerializer(obj)
            return Response({"status":status.HTTP_200_OK,"data":serializer.data})
        except Exception as e:
            print(e)
            return Response("Failed")

    def put(self,request,format=None):
        pass

class Questions(APIView):
    
    def post(self,request,format=None):
        data=request.data
        secret_key = data.get('secret_key',None)
        qid = data.get('qid',None)
        user_id = data.get('user_id',None)
        if secret_key==None or user_id ==None:
            return Response({"status":'404',"data":"Record Not Found"})
        if qid == None:
            try:
                obj= Question.objects.all()
                data = []
                if obj != None:
                    for ques in obj:
                        quesJson = QuestionSerializer(ques).data;
                        options = Options.objects.filter(qid=quesJson.get('id'))
                        data.append({
                            "ques": quesJson,
                            "options":OptionSerializer(options,many=True).data
                        })
                    return Response({"status":status.HTTP_200_OK,"data": data})
            except Exception as e:
                print(e)
                return Response("Failed")
            

    def put(self,request,format=None):
        pass

class Answers(APIView):
    def post(self,request,format=None):
        data = request.data
        answer = data.get('answer',None)
        if answer == None:
            return  Response({"status":status.HTTP_200_OK,"data": []})
        else:
            correct = 0
            wrong = 0
            coin = 0
            try:
                for obj in answer:
                    qid = int(obj.get('qid',None))
                    oid = int(obj.get('ans',None))
                    ans = Answer.objects.get(qid=qid)
                    ansSerial = AnswerSerializer(ans).data
                    quesObj = Question.objects.get(id=qid)
                    quesSerial = QuestionSerializer(quesObj).data
                    print(ansSerial)
                    if ansSerial.get('option_id',None) == oid:
                        correct = correct + 1
                        coin = coin + quesSerial.get('coins',0)
                return Response({"status":status.HTTP_200_OK, "data": {"correct":correct,"wrong":len(answer) - correct,"coin":coin}})
            except Exception as e:
                return Response({"status":500,data:[]})

class Quiz(APIView):
    def get(self,request,qid=None,format=None):
        if qid != None:
            try:
                obj= Question.objects.filter(quiz_id = qid)
                data = []
                if obj != None:
                    for ques in obj:
                        quesJson = QuestionSerializer(ques).data;
                        options = Options.objects.filter(qid=quesJson.get('id'))
                        data.append({
                            "ques": quesJson,
                            "options":OptionSerializer(options,many=True).data
                        })
                    return Response({"status":status.HTTP_200_OK,"data": data})
            except Exception as e:
                print(e)
                return Response("Failed")
            
    def post(self,request,format=None):
        data = request.data 
        user_id = data.get('user_id',None)
        print(user_id)
        if user_id == None:
            return Response({"status":status.HTTP_200_OK, "data": []})
        else:
            try:
                takenQuiz = QuizTaken.objects.filter(user_id=user_id)
                jsonQuiz = QuizTakenSerializer(takenQuiz,many=True).data
                data = Quizs.objects.exclude(id__in = [obj.get('quiz_id') for obj in jsonQuiz])
                quizserial = QuizSerializer(data,many=True)
                return Response({"status":status.HTTP_200_OK, "data": quizserial.data})
                pass
            except Exception as e:
                print(e)
                return Response({"status":500, "data": []})
                pass
class PaymentDetail(APIView):
    def get(self,request,id,format=None):
        if id ==None:
            return Response({"status":status.HTTP_200_OK, "data": []})
        try:
            obj = UserPaymentOptions.objects.filter(user_id=id)
            print(obj)
            serializer = UserPaymentOptionsSerializer(obj,many=True)
            return Response({"status":status.HTTP_200_OK, "data": serializer.data})
        except Exception as e:
            return Response({"status":status.HTTP_200_OK, "data": e})
    def post(self,request,id,format=None):
        data = request.data 
        user_id = data.get('user_id',None)
        if user_id != None:
            try:
                serializer = UserPaymentOptionsSerializer(data=data)
                print(serializer.is_valid())
                if serializer.is_valid():
                    serializer.save()
                    return Response("created")
            except Exception as e:
                return Response(e)
            
            
