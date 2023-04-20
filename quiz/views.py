from email.policy import HTTP
from functools import partial
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import json
from .models import User,UserPaymentOptions,PaymentDetails,PaymentProvider,OrderDetails,Question,QuestionTag,Options,Answer,QuizTaken,Quizs,CreditDebit
from .serializer import UserSerializer,UserPaymentOptionsSerializer,PaymentDetailsSerializer,PaymentProviderSerializer,OrderSerializer,QuestionSerializer,QuestionTagSerializer,OptionSerializer,AnswerSerializer,QuizSerializer,QuizTakenSerializer,CreditDebitSerializer
from django.http import JsonResponse
from django.db.models import Sum
from django.db.models import F, Count, Value
from django.db.models import Q
class Users(APIView):
    def post(self,request,format=None):
        data=request.data
        print(data)
        user_id = data.get('user_id',None)
        if(user_id != None):
            try:
                obj = User.objects.get(user_id = user_id)
                serializer = UserSerializer(obj,data=data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                return self.get(request,user_id)

            except Exception as e:
                serailizer=UserSerializer(data=data)
                if serailizer.is_valid():
                    serailizer.save()
                    return self.get(request,user_id)
        return Response({status:status.HTTP_400_BAD_REQUEST,"msg":"Failed"})
    
    def get(self,request,id,format=None):
        if id==None:
            return Response({"status":'404',"data":"Record Not Found"})

        try:
            obj=User.objects.get(user_id=id)
            payData = None
            try:
                payment_details = UserPaymentOptions.objects.get(user_id=obj)
                paymentSerial = UserPaymentOptionsSerializer(payment_details)
                payData = paymentSerial.data
                # print(paymentSerial.data)
                # for pay in paymentSerial:
                #     if str(pay.get('user_id')) == str(id):
                #         payData = pay 
                #         break
            except Exception as e:
                pass
            serializer=UserSerializer(obj)
            
            return Response({"status":status.HTTP_200_OK,"data":{"user":serializer.data,"paymetDetails":payData}})
        except Exception as e:
            print(e)
            return Response({"status":500,"msg":"Failed"})

    def put(self,request,format=None):
        data = request.data
        print("in put",data)
        try:
            userObj = User.objects.get(user_id = data.get('user_id'))
            serializer = UserSerializer(userObj,data=data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return self.get(request,data.get('user_id'))
        except Exception as e:
            return Response({"status":400,"data":"Update failed"})

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
        print(data)
        answer = data.get('answer',None)
        user_id = data.get('user_id',None)
        quiz_id = data.get('quiz_id',None)
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
                user_ob = User.objects.get(user_id = user_id)
                quiz_obj = Quizs.objects.get(id = quiz_id)
                user = UserSerializer(user_ob).data
                allowed = user.get('quiz_allowed',3)
                total_coins = user.get('total_coins',0)
                if user.get('quiz_allowed',0)>0:
                    User.objects.filter(user_id = user_id).update(quiz_allowed = allowed-1, total_coins=total_coins+coin)
                    QuizTaken.objects.create(user_id=user_ob,quiz_id=quiz_obj,correct_ans=correct,incorrect_ans=len(answer) - correct,earned_coins=coin)
                # QuizTaken.objects.create(data=quizsTaken)
                    CreditDebit.objects.create(user_id=user_ob,credit=coin)
                return Response({"status":status.HTTP_200_OK, "data": {"correct":correct,"wrong":len(answer) - correct,"coin":coin}})
            except Exception as e:
                return Response({"status":500,data:[]})

class Quiz(APIView):
    def get(self,request,qid=None,type=None,format=None):
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
        quiz_type = data.get('quiz_type',None)
        print(user_id)
        if user_id == None:
            return Response({"status":status.HTTP_200_OK, "data": []})
        else:
            try:
                takenQuiz = QuizTaken.objects.filter(user_id=user_id)
                jsonQuiz = QuizTakenSerializer(takenQuiz,many=True).data
                data = Quizs.objects.filter(quiz_type=quiz_type).exclude(id__in = [obj.get('quiz_id') for obj in jsonQuiz])
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
            user_obj = User.objects.get(user_id =id)
            obj = UserPaymentOptions.objects.get(user_id=user_obj)
            serializer = UserPaymentOptionsSerializer(obj)
            return Response({"status":status.HTTP_200_OK, "data": serializer.data})
        except Exception as e:
            return Response({"status":status.HTTP_200_OK, "data": e})
    def post(self,request,id,format=None):
        data = request.data 
        user_id = data.get('user_id',None)
        user_obj = User.objects.get(user_id =id)
        try:
            pay_exists = UserPaymentOptions.objects.get(user_id=user_obj)
            self.put(request,id)
            return self.get(request,id)
        except Exception as e:
            
            if user_id != None:
                try:
                    serializer = UserPaymentOptionsSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return self.get(request,id)
                except Exception as e:
                    return Response(e)
    def put(self,request,id,format=None):
        data = request.data 
        print(data)
        user_id = data.get('user_id',None)
        if user_id != None:
            try:
                user_obj = User.objects.get(user_id=id)
                pay_obj = UserPaymentOptions.objects.get(user_id = user_obj);
                provider = PaymentProvider.objects.get(id=data.get('provider',1))
                data['provider'] = provider
                # serializer = UserPaymentOptionsSerializer(pay_obj,data=data,partial=True)
                UserPaymentOptions.objects.filter(user_id=user_obj).update(name=data.get('name',''),provider=provider,payment_num=data.get('payment_num'));
                # if serializer.is_valid():
                #     print("valid")
                #     serializer.save()
                    # return self.get(request,id)
                return self.get(request,id)
            except Exception as e:
                return Response({"status":"500"})

class UserPaymentOption(APIView):
    def get(self,request,format=None):
        data = request.data 
        user_id = data.get('user_id',None)
        if user_id != None:
            try:
                paymentOption = UserPaymentOptions.objects.get(user_id=user_id)
                serial = UserPaymentOptionsSerializer(paymentOption)
                return  Response({"status":status.HTTP_200_OK, "data": serial.data})
            except Exception as e:
                return  Response({"status":status.HTTP_200_OK, "data": e})
    def post(self,request,format=None):
        # provider = {paytm:1,phonePe:2}
        data = request.data 
        try:
            payment = UserPaymentOptionsSerializer(data = data)
            if payment.is_valid():
                payment.save()
                return Response({"status":status.HTTP_200_OK, "data": "created"})
        except Exception as e:
            return  Response({"status":status.HTTP_200_OK, "data": e})
    def put(self,request,format=None):
        data = request.data
        try:
            payment = UserPaymentOptionsSerializer(data = data,partial=True)
            if payment.is_valid():
                payment.save()
                return Response({"status":status.HTTP_200_OK, "data": "created"})
        except Exception as e:
            return  Response({"status":status.HTTP_200_OK, "data": e})

class UserHistory(APIView):
    def get(self,request,user_id,format=None): 
        print(user_id)
        try:
            data = CreditDebit.objects.filter(user_id=user_id).order_by('-created_at')
            serial = CreditDebitSerializer(data,many=True)
            orderedData = serial.data
            for obj in orderedData:
                if obj.get('order_details',None) != None:
                    order_status = OrderDetails.objects.get(order_id = obj.get('order_details',None)).status
                    obj['status'] = order_status
            credit = CreditDebit.objects.filter(user_id=user_id).aggregate(Sum('credit'))['credit__sum']
            debit = CreditDebit.objects.filter(user_id=user_id).aggregate(Sum('debit'))['debit__sum']
            if credit ==None:
                credit = 0
            if debit == None:
                debit = 0
            available_coin = credit - debit
            return  Response({"status":status.HTTP_200_OK, "data": {"history":orderedData,"total_earned_coin":credit,"available_coin":available_coin}})
        except Exception as e:
            return  Response({"status":status.HTTP_200_OK, "data": e})

class OrderDetail(APIView):
    def post(self,request,format=None):
        data = request.data
        user_id = data.get('user_id',None)
        ammount_request = int(data.get('ammount_requested',0))
        print(data)
        if(user_id == None):
            return Response({"status":status.HTTP_200_OK, "data": "No data found"})
        try:
            # resp = OrderDetails.objects.create(data=data)
            serial = OrderSerializer(data=data)
            if serial.is_valid():
                print("Valid")
                # serial.save()
                user_obj = User.objects.get(user_id=user_id)
                total_coins =int( User.objects.get(user_id=user_id).total_coins)
                print(int(total_coins)>int(ammount_request))
                if int(total_coins) < int(ammount_request):
                    return Response({"status":"500", "data": "Can not withdraw more than available"})
                User.objects.filter(user_id=user_id).update(total_coins= total_coins-ammount_request);
                serial.save()
                order_obj = OrderDetails.objects.get(order_id = data.get('order_id'));
                CreditDebit.objects.create(user_id=user_obj,debit=ammount_request,order_details=order_obj)
                return Response({"status":status.HTTP_200_OK, "data": "ordered"})
            return Response({"status":500, "data": "failed"})
        except Exception as e:
            return  Response({"status":500, "data": e})

class LeaderBoard(APIView):
    def get(self,request,format=None):
        try:
            obj = CreditDebit.objects.all().filter(~Q(credit = 0)).order_by('-credit') #.distinct('user_id')
            # obj = CreditDebit.objects.aaggregate(credit_sum = Sum('credit')).order_by('-credit_sum').distinct('user_id')
            serail = CreditDebitSerializer(obj,many=True)
            data = serail.data 
            for obj in data:
                user_obj = User.objects.get(user_id = obj.get('user_id'))
                userSerial = UserSerializer(user_obj).data
                print(userSerial)
                obj['profile_pic'] = userSerial.get('profile_pic',None)
            return Response({"status":status.HTTP_200_OK, "data": data})  
        except Exception as e:
            return Response({"status":status.HTTP_200_OK, "data": e})  




            
            
