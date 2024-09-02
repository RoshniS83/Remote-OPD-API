from django.shortcuts import render
from villages.models import Villages
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django.http import HttpResponse
from rest_framework.response import Response
from villages.serializers import VillageSerializer

# Create your views here.
class VillagesAPI(ModelViewSet):
    queryset=Villages.objects.all()
    serializer_class = VillageSerializer

    def list(self, request, *args, **kwargs):
        try:
            allvillages = Villages.objects.all()
            serializer = self.get_serializer(allvillages, many=True)
            formatted_data = []
            for village in serializer.data:
                vnames = village.get('vnames', ' ')
                formatted_Villages = {'id' : village['id'],'name': village['name'], 'vnames': [subvillage.strip() for subvillage in vnames.split(',')] if vnames else []}
                formatted_data.append(formatted_Villages)

            api_response = { 'status' : 'success',
                             'code': status.HTTP_200_OK,
                             'message':'All Villages',
                             'all_Villages': formatted_data
                             }
            return Response(api_response)
        except Exception as e:
            error_message = f'An error occurred while fetching Villages: {str(e)}'
            error_response = {
                'status' : 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': error_message
            }
            return Response(error_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve_byname(self, request, *args, **kwargs):
        name = kwargs.get('name')

        try:
            instance = Villages.objects.get(name=name)
            serializer = self.get_serializer(instance)
            village_data = serializer.data
            formatted_data = []
            # for village_data in serializer.data:

            vnames = village_data.get('vnames',' ')

            formatted_villages = {
                        'id': village_data['id'],
                        'name': village_data['name'],
                        'vnames': [subvillage.strip() for subvillage in vnames.split(',')] if vnames else []
                    }
            formatted_data.append(formatted_villages)
            api_response = {
                'status':'success',
                'code':status.HTTP_200_OK,
                'message':'SubVillages list by village name',
                'subvillages': formatted_data
            }
            return Response(api_response)
        except Villages.DoesNotExist:
            error_response={ 'status':'error',
                             'code':status.HTTP_404_NOT_FOUND,
                             'message': 'Village not found'}
            return Response(error_response)
        except Exception as e:
            error_message = f'An error occurred while fetching the village record :{str(e)}  '
            error_response = {'status':'error',
                              'code':status.HTTP_500_INTERNAL_SERVER_ERROR,
                              'message':error_message}
            return Response(error_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)







    def retrieve(self, request, *args, **kwargs):
        try:
            instance= self.get_object()
            serializer = self.get_serializer(instance)
            sub_villages = serializer.data.get('vnames','')
            formatted_Villages = {
                'id':serializer.data['id'],
                'name': serializer.data['name'],
                'vnames': [subvillage.strip() for subvillage in sub_villages.split(',')] if sub_villages else []
            }
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message' : 'Villages retrieved successfully',
                'Villages': formatted_Villages
            }
            return Response(api_response)
        except Exception as e:
            error_message = f'An error occurred while fetching the Villages: {str(e)}'
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
            serializer.save()

            api_response = {
                'status': 'success',
                'code':status.HTTP_201_CREATED,
                'message':'Villages created successfully',
                'Villages':serializer.data
            }
            return Response(api_response, status=status.HTTP_201_CREATED)
        except Exception as e:
            error_message = f'An error occured while creating Villages: {str(e)}'
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
                'message': 'Villages updated successfully',
                'Villages': serializer.data
                 }
            return Response(api_response)
        except Exception as e:
            error_message= f'An error occured while updating the Villages: {str(e)}'
            error_response = {
                'status':'error',
                'code':status.HTTP_400_BAD_REQUEST,
                'message': error_message
            }
            return Response(error_response, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        try:
            kwargs['partial'] = True
            response =self.update(request, *args, **kwargs)
            api_response ={
                'status':'success',
                'code':status.HTTP_200_OK,
                'message':'Villages list updated partially',
                'updated_village_list': response.data
            }
            return Response(api_response, status=status.HTTP_200_OK)
        except Exception as e:
            error_message = f'Error while updating village list {str(e)}'
            error_response = {
                'status':'error',
                'code':status.HTTP_400_BAD_REQUEST,
                'message':error_message
            }
            return Response(error_response, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            village = self.get_object()
            village.delete()

            api_response = {
                'status': 'success',
                'code':status.HTTP_204_NO_CONTENT,
                'message': 'Villages deleted successfully'
            }
            return Response(api_response, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            error_message= f'An error occurred while deleting the Villages: {str(e)}'
            error_response = {
                'status':'error',
                'code':status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message':error_message
            }
            return Response(error_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




