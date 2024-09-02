import datetime

import openpyxl
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from Patient.models import Patientopdform
from Patient.serializers import PatientSerializer

# Create your views here.
class PatientAPI(ModelViewSet):
    queryset = Patientopdform.objects.all()
    serializer_class = PatientSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {            'status': 'success',
                                        'code': status.HTTP_201_CREATED,
                                        'message': 'Patient OPD form added successfully',
                                        'new_form': serializer.data,
                            }
            return Response(api_response)
        except Exception as e:
            error_message = 'Failed to add patient opd form: {}'.format(str(e))
            error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_400_BAD_REQUEST,
                                        'message': error_message
                              }
            return Response(error_response)

    def retrieve (self, request, *args, **kwargs):
        try:
            instance=self.get_object()
            serializer=self.serializer_class(instance)
            api_response = { 'status' : 'success',
                             'code': status.HTTP_200_OK,
                             'patient': serializer.data }
            return Response(api_response)
        except Exception as e:
            error_message = 'Failed to retrieve patient opd form: {}'.format(str(e))
            error_response = {
                'status':'error',
                'code':status.HTTP_404_NOT_FOUND,
                'message': error_message
                }
            return Response(error_response)

    def update(self, request,*args, **kwargs):
        try:
            partial=kwargs.pop('partial',False)
            instance = self.get_object()
            serializer= self.serializer_class(instance, data= request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            api_response = {
                'status':'success',
                'code':status.HTTP_200_OK,
                'message':'Patient OPD form updated successfully',
                'updated_form' : serializer.data
            }
            return Response(api_response)
        except Exception as e:
            error_message = 'Failed to update patient opd form:{}'. format(str(e))
            error_response ={
                'status':'error',
                'code':status.HTTP_400_BAD_REQUEST,
                'message': error_message
            }
            return  Response(error_response)

    def partial_update(self, request, *args, **kwargs):
        try:
            kwargs['partial'] = True
            response= self.update(request, *args, **kwargs)
            api_response = {
                'status':'success',
                'code':status.HTTP_200_OK,
                'message':'Patient OPD form updated successfully',
                'updated_form': response.data
            }
            return Response(api_response, status=status.HTTP_200_OK)
        except Exception as e:
            error_message =f'Failed to partially update patient opd form: {str(e)} '
            error_response={
                'status':'error',
                'code':status.HTTP_400_BAD_REQUEST,
                'message': error_message
            }
            return Response(error_response)

    def destroy(self, request,*args, **kwargs):
        try:
            instance= self.get_object()
            instance.delete()
            api_response = {
                'status':'success',
                'code': status.HTTP_204_NO_CONTENT,
                'message':'Patient OPD form deleted successfully'
            }
            return Response(api_response)
        except Exception as e:
            error_message= 'Failed to delete patient opd form {}'. format(str(e))
            error_response= {
                'status':'error',
                'code':status.HTTP_400_BAD_REQUEST,
                'message':error_message
            }
            return Response(error_response)

    def list(self, request, *args, **kwargs):
        try:
            queryset=self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            api_response ={
                'status':'success',
                'code':'status.HTTP_200_OK',
                'patients': serializer.data
            }
            return Response(api_response)
        except Exception as e:
            error_message= f'Failed to retrieve patient opd forms :{str(e)}'
            error_response = {
                'status':'error',
                'code':status.HTTP_400_BAD_REQUEST,
                'message':error_message
            }
            return Response(error_response)


class ExcelReport(APIView):
          def get(self, request):
                    data = Patientopdform.objects.all()  # Query data

                    # Mapping of attribute names to display names
                    headers_mapping = {
                              'srNo': 'Sr.No.',
                              'patientName': 'Patient Name',
                              'date': 'Date',
                              'villageName': 'Village Name',
                              'category': 'N/F/SC/R',
                              'gender': 'Gender',
                              'age': 'Age',
                              'day': 'Day',
                              'month': 'Month',
                              'ageGroup': 'Age Group',
                              'week': 'Week',
                              'mobileNo': 'Mobile No.',
                              'signSymptoms': 'Sign and Symptoms',
                              'physicalExamination': 'Physical Examination and Finding',
                              'investigation': 'Investigation',
                              'diagnosis': 'Diagnosis',
                              'prescribedMedicine1': 'Prescribed medicine 1',
                              'prescribedMedicine2': 'Prescribed medicine 2',
                              'dosage': 'Dosage',
                              'treatmentRemark': 'Treatment Remark',
                    }

                    # Initialize Excel workbook and sheet
                    wb = openpyxl.Workbook()
                    ws = wb.active

                    # Write headers
                    headers = list(headers_mapping.values())
                    ws.append(headers)

                    # Write data rows
                    for row in data:
                              row_data = [getattr(row, field) for field in headers_mapping.keys()]
                              ws.append(row_data)

                    # Get the current date
                    current_date = datetime.date.today().strftime('%Y-%m-%d')

                    # Create HttpResponse object with Excel content type
                    response = HttpResponse(
                              content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                    response['Content-Disposition'] = f'attachment; filename="Shirwal OPD {current_date}.xlsx"'

                    # Save the Excel file to the HttpResponse
                    wb.save(response)
                    return response
