from django.shortcuts import render
from disease.models import Disease
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django.http import HttpResponse
from rest_framework.response import Response
from disease.serializers import DiseaseSerializer

# Create your views here.
class DiseaseAPI(ModelViewSet):
    queryset=Disease.objects.all()
    serializer_class = DiseaseSerializer

    def list(self, request, *args, **kwargs):
        try:
            diseases= Disease.objects.all()
            serializer = self.get_serializer(diseases, many=True)
            formatted_data = []
            for disease in serializer.data:
                formatted_disease = {'id' : disease['id'],'name': disease['name']}
                formatted_data.append(formatted_disease)

            api_response = { 'status' : 'success',
                             'code': status.HTTP_200_OK,
                             'message':'All Diseases',
                             'all_diseases': formatted_data
                             }
            return Response(api_response)
        except Exception as e:
            error_message = f'An error occurred while fetching diseases: {str(e)}'
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
            formatted_disease = {
                'id':serializer.data['id'],
                'name': serializer.data['name']
            }
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message' : 'Disease retrieved successfully',
                'disease': formatted_disease
            }
            return Response(api_response)
        except Exception as e:
            error_message = f'An error occurred while fetching the disease: {str(e)}'
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
                'message':'Disease created successfully',
                'disease':serializer.data
            }
            return Response(api_response, status=status.HTTP_201_CREATED)
        except Exception as e:
            error_message = f'An error occured while creating disease: {str(e)}'
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
                'message': 'Disease updated successfully',
                'disease': serializer.data
                 }
            return Response(api_response)
        except Exception as e:
            error_message= f'An error occured while updating the disease: {str(e)}'
            error_response = {
                'status':'error',
                'code':status.HTTP_400_BAD_REQUEST,
                'message': error_message
            }
            return Response(error_response, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            disease = self.get_object()
            disease.delete()

            api_response = {
                'status': 'success',
                'code':status.HTTP_204_NO_CONTENT,
                'message': 'Disease deleted successfully'
            }
            return Response(api_response, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            error_message= f'An error occurred while deleting the disease: {str(e)}'
            error_response = {
                'status':'error',
                'code':status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message':error_message
            }
            return Response(error_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

