from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
import math
import requests
from calculator.Serializer import EnrollerSerializer
from rest_framework.decorators import api_view 
# Create your views #siubmit 
@api_view(['POST'])
def submit_info(request):
    print("inside the submit info")
    print(request.data)
    serializer=EnrollerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Submission_msg":"submit details has been done"},status=201)
                            
    return Response(serializer.errors,status=400)



# @api_view(['POST'])
# def submit_info(request):
#     print("inside the submit info")
#     serializer = EnrollerSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"submission_msg": "Details have been successfully submitted!"}, status=201)
#     return Response(serializer.errors, status=400)
@api_view(['GET'])
def check_api(request):
    return HttpResponse("hello apis ")

@api_view(['POST'])
def emi_calc(request):
    loan_amt= int(request.data.get('loan_amount'))
    tenure= int(request.data.get('tenure'))
    interset_amt= float(request.data.get('intrest_rate'))
    rate_normalise=interset_amt/12/100
    emi_amt= (loan_amt*rate_normalise*math.pow(1+rate_normalise,tenure))/(math.pow(1+rate_normalise,tenure)-1)
    principal_amt=loan_amt
    tot_amt=emi_amt*tenure
    interset_amt=tot_amt-loan_amt
    return Response({'emi':emi_amt,'principal_amt':principal_amt,'total_amt':tot_amt,'interest_amt':interset_amt})



  
# #secon api 
# req(l,t,i)--->(Monthly Home Loan EMI
# ₹19,668
# View Details
# Principal Amount
# ₹25,00,000
# Interest Amount
# ₹45,80,304
# Total Amount Payable
# ₹70,80,304
# Need more information?) 
