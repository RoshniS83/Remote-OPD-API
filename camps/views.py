from django.shortcuts import render
from camps.models import Camps
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django.http import HttpResponse
from rest_framework.response import Response
from camps.serializers import CampsSerializer

# Create your views here.
class CampsAPI(ModelViewSet):
    queryset=Camps.objects.all()
    serializer_class = CampsSerializer

    def list(self, request, *args, **kwargs):
        try:
            camp= Camps.objects.all()
            serializer = self.get_serializer(camp, many=True)
            formatted_data = []
            for camp in serializer.data:
                formatted_Camps = {'id' : camp['id'], 'name': camp['name']}
                formatted_data.append(formatted_Camps)

            api_response = { 'status': 'success',
                             'code': status.HTTP_200_OK,
                             'message': 'All Camps',
                             'all_Camps': formatted_data
                             }
            return Response(api_response)
        except Exception as e:
            error_message = f'An error occurred while fetching Camps: {str(e)}'
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
            formatted_Camps = {
                'id': serializer.data['id'],
                'name': serializer.data['name']
            }
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message' : 'Camps retrieved successfully',
                'Camps': formatted_Camps
            }
            return Response(api_response)
        except Exception as e:
            error_message = f'An error occurred while fetching the Camps: {str(e)}'
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
                'message':'Camps created successfully',
                'Camps':serializer.data
            }
            return Response(api_response, status=status.HTTP_201_CREATED)
        except Exception as e:
            error_message = f'An error occured while creating Camps: {str(e)}'
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
                'message': 'Camps updated successfully',
                'Camps': serializer.data
                 }
            return Response(api_response)
        except Exception as e:
            error_message= f'An error occured while updating the Camps: {str(e)}'
            error_response = {
                'status':'error',
                'code':status.HTTP_400_BAD_REQUEST,
                'message': error_message
            }
            return Response(error_response, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            Camps = self.get_object()
            Camps.delete()

            api_response = {
                'status': 'success',
                'code':status.HTTP_204_NO_CONTENT,
                'message': 'Camps deleted successfully'
            }
            return Response(api_response, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            error_message= f'An error occurred while deleting the Camps: {str(e)}'
            error_response = {
                'status':'error',
                'code':status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message':error_message
            }
            return Response(error_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



