from django.shortcuts import render
from medicines.models import Medicines
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django.http import HttpResponse
from rest_framework.response import Response
from medicines.serializers import MedicineSerializer

# Create your views here.
class MedicinesAPI(ModelViewSet):
    queryset=Medicines.objects.all()
    serializer_class =MedicineSerializer

    def list(self, request, *args, **kwargs):
        try:
            mediciness= Medicines.objects.all()
            serializer = self.get_serializer(mediciness, many=True)
            formatted_data = []
            for medicines in serializer.data:
                formatted_medicines = {'id' : medicines['id'],'name': medicines['name']}
                formatted_data.append(formatted_medicines)

            api_response = { 'status' : 'success',
                             'code': status.HTTP_200_OK,
                             'message':'All mediciness',
                             'all_mediciness': formatted_data
                             }
            return Response(api_response)
        except Exception as e:
            error_message = f'An error occurred while fetching medicines: {str(e)}'
            error_response = {
                'status' : 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': error_message
            }
            return Response(error_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance= self.get_object()
            serializer = self.get_serializer(instance)
            formatted_medicines = {
                'id':serializer.data['id'],
                'name': serializer.data['name']
            }
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message' : 'medicines retrieved successfully',
                'medicines': formatted_medicines
            }
            return Response(api_response)
        except Exception as e:
            error_message = f'An error occurred while fetching the medicines: {str(e)}'
            error_response ={
                'status' : 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': error_message
            }
            return Response(error_response, status= status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            api_response = {
                'status': 'success',
                'code':status.HTTP_201_CREATED,
                'message':'medicines created successfully',
                'medicines':serializer.data
            }
            return Response(api_response, status=status.HTTP_201_CREATED)
        except Exception as e:
            error_message = f'An error occured while creating medicines: {str(e)}'
            error_response ={
                'status':'error',
                'code':status.HTTP_400_BAD_REQUEST,
                'message':error_message
            }
            return Response(error_response, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception =True)
            self.perform_update(serializer)
            api_response={
                'status':'success',
                'code': status.HTTP_200_OK,
                'message': 'medicines updated successfully',
                'medicines': serializer.data
                 }
            return Response(api_response)
        except Exception as e:
            error_message= f'An error occured while updating the medicines: {str(e)}'
            error_response = {
                'status':'error',
                'code':status.HTTP_400_BAD_REQUEST,
                'message': error_message
            }
            return Response(error_response, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            medicines = self.get_object()
            medicines.delete()

            api_response = {
                'status': 'success',
                'code':status.HTTP_204_NO_CONTENT,
                'message': 'medicines deleted successfully'
            }
            return Response(api_response, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            error_message= f'An error occurred while deleting the medicines: {str(e)}'
            error_response = {
                'status':'error',
                'code':status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message':error_message
            }
            return Response(error_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




