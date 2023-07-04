from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from myapp.models import Contact,LeaveRequest
from myapp.serializer import ContactSerializer,LeaveSerializer,LeavebySerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics


"""
class api_list(generics.ListCreateAPIView):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer
"""
@api_view(['GET','POST'])
def api_list(request):
   
    if request.method == 'GET':
        apivar = Contact.objects.all()
        serializer = ContactSerializer(apivar, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    
@api_view(['GET','POST'])
def  leave_list(request):
   
    if request.method == 'GET':
        apivar = LeaveRequest.objects.all()
        serializer = LeaveSerializer(apivar, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LeaveSerializer(data=request.data)
        if serializer.is_valid():
            employee_id = request.data.get('employee')
            count = LeaveRequest.objects.filter(employee=employee_id).count()
            print('count:', count)
            if count > 3:
                return Response('You can not request more than 4 times')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""

class api_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer

"""
@api_view(['GET', 'PUT', 'DELETE'])
def api_detail(request, pk):
   
    try:
        apivar = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContactSerializer(apivar)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ContactSerializer(apivar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        apivar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'PUT', 'DELETE'])
def leave_detail(request, pk):
   
    try:
        apivar = LeaveRequest.objects.get(pk=pk)
    except LeaveRequest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LeaveSerializer(apivar)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = LeaveSerializer(apivar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        apivar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_vacation_status(request,pk):
     try:
        apivar = LeaveRequest.objects.get(pk=pk)
     except LeaveRequest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
     serializer = LeaveSerializer(apivar)
     return Response(serializer.data['status'],status=status.HTTP_200_OK)

@api_view(['GET'])
def get_vacation_count(request,pk):
     count = LeaveRequest.objects.filter(employee=pk).count()
     if count:
        response_data = {
                    'message': f"Number of times requested for leave: {count}"
                }
        return Response( response_data,status=status.HTTP_200_OK)
     else :
         return Response('This user not exit ', status=status.HTTP_400_BAD_REQUEST)
     
@api_view(['GET'])
def get_all_about(request,pk):
    try:
        apv=Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = LeavebySerializer(apv)
    return Response(serializer.data,status=status.HTTP_200_OK)

 
 