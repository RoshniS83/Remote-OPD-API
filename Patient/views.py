import datetime
import io

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
import openpyxl
from openpyxl.utils import get_column_letter
from django.http import HttpResponse
import datetime
from Patient.models import Patientopdform
from Patient.serializers import PatientSerializer
import pandas as pd
from datetime import datetime
import os
from django.conf import settings
from django.http import FileResponse
from openpyxl.styles import Border, Side
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



#This WeeksExcelSheet class is dividing the whole excelsheet data of all months from Apr to August into Weeks - Now we are commenting it for future use
# class WeeksExcelSheet(APIView):
#     def get(self, request):
#         # Query data from Patientopdform model
#         data = Patientopdform.objects.all()  # Query data
#
#         # Mapping of attribute names to display names
#         headers_mapping = {
#             'srNo': 'Sr.No.',
#             'patientName': 'Patient Name',
#             'date': 'Date',
#             'villageName': 'Village Name',
#             'camp_name':'Camp Name',
#             'category': 'N/F/SC/R',
#             'gender': 'Gender',
#             'age': 'Age',
#             'day': 'Day',
#             'month': 'Month',
#             'ageGroup': 'Age Group',
#             'week': 'Week',
#             'mobileNo': 'Mobile No.',
#             'signSymptoms': 'Sign and Symptoms',
#             'physicalExamination': 'Physical Examination and Finding',
#             'investigation': 'Investigation',
#             'diagnosis': 'Diagnosis',
#             'prescribedMedicine1': 'Prescribed medicine 1',
#             'prescribedMedicine2': 'Prescribed medicine 2',
#             'dosage': 'Dosage',
#             'treatmentRemark': 'Treatment Remark',
#         }
#         media_path = settings.MEDIA_ROOT
#         if not os.path.exists(media_path):
#             os.makedirs(media_path)
#         # Initialize Excel workbook
#         wb = openpyxl.Workbook()
#
#         # Separate data for each week
#         weeks = data.values_list('week', flat=True).distinct()
#
#         for week in weeks:
#             ws = wb.create_sheet(title=f'Week {week}')
#             # Write headers
#             headers = list(headers_mapping.values())
#             ws.append(headers)
#
#             # Filter data by week
#             week_data = data.filter(week=week)
#
#             # Write data rows for that week
#             for row in week_data:
#                 row_data = [getattr(row, field) for field in headers_mapping.keys()]
#                 ws.append(row_data)
#
#         # Remove the default sheet created by openpyxl (if empty)
#         if 'Sheet' in wb.sheetnames:
#             default_sheet = wb['Sheet']
#             wb.remove(default_sheet)
#
#         # Get the current date
#         current_date = datetime.today().strftime('%Y-%m-%d')
#         file_path = os.path.join(media_path, f'Weeks_wise_report{current_date}.xlsx')
#         wb.save(file_path)
#         # Create HttpResponse object with Excel content type
#         response = HttpResponse(
#             content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
#         )
#         response['Content-Disposition'] = f'attachment; filename="Weeks_wise_report{current_date}.xlsx"'
#
#         # Save the Excel file to the HttpResponse
#         response.write(f'File saved successfully: {file_path}')
#         return response



#This WeeklyExcelReport class is generating the Report data from Week-wise-report(media folder)- Now we are commenting it for future use
# class WeeklyExcelReport(APIView):
#     def get(self, request):
#         # Query data from Patientopdform model
#         data = Patientopdform.objects.all()
#
#         # Mapping of attribute names to display names
#         headers_mapping = {
#             'srNo': 'Sr.No.',
#             'patientName': 'Patient Name',
#             'date': 'Date',
#             'villageName': 'Village Name',
#             'camp_name': 'Camp Name',
#             'category': 'N/F/SC/R',
#             'gender': 'Gender',
#              'age': 'Age',
#              'day': 'Day',
#              'month': 'Month',
#              'ageGroup': 'Age Group',
#              'week': 'Week',
#              'mobileNo': 'Mobile No.',
#              'signSymptoms': 'Sign and Symptoms',
#              'physicalExamination': 'Physical Examination and Finding',
#              'investigation': 'Investigation',
#              'diagnosis': 'Diagnosis',
#              'prescribedMedicine1': 'Prescribed medicine 1',
#              'prescribedMedicine2': 'Prescribed medicine 2',
#              'dosage': 'Dosage',
#              'treatmentRemark': 'Treatment Remark',
#         }
#
#         # Create a week-wise dictionary to hold dataframes
#         weeks_dataframes = {}
#
#         # Separate data for each week
#         weeks = data.values_list('week', flat=True).distinct()
#
#         # Create dataframe for each week
#         for week in weeks:
#             # Filter data by week
#             week_data = data.filter(week=week)
#
#             # Create dataframe for the current week
#             df = pd.DataFrame(list(week_data.values(*headers_mapping.keys())))
#             # Ensure column names are consistent
#             df.columns = [headers_mapping.get(col, col) for col in df.columns]
#             # Store dataframe in dictionary
#             weeks_dataframes[week] = df
#
#         # Initialize an Excel writer for output
#         output = io.BytesIO()
#         with pd.ExcelWriter(output, engine='openpyxl') as writer:
#             # Process each week's dataframe
#             for week, df in weeks_dataframes.items():
#                 if df.empty:
#                     continue
#
#                 # Create a 'Count' column with value 1
#                 df['Count'] = 1
#                 # Ensure that 'Day' is in the DataFrame
#                 if 'Day' not in df.columns:
#                     print(f"Day column not found in Week {week}")
#                     continue
#                 # Create pivot table for the current week
#                 try:
#                     pivot_table = df.pivot_table(
#                         index='diagnosis',
#                         columns=['day', 'villageName', 'gender'],
#                         values='Count',
#                         aggfunc='sum',
#                         fill_value=0
#                     )
#                 except KeyError as e:
#                     # Skip this sheet if required columns are missing
#                     print(f"Skipping week {week} due to missing column: {e}")
#                     continue
#
#                 # Reset the index to make 'Diagnosis' the first column
#                 pivot_table.reset_index(inplace=True)
#
#                 # Write the pivot table to a new sheet in the output Excel file
#                 pivot_table.to_excel(writer, sheet_name=f'Weekly Report - Week {week}', index=True)
#
#         # Create HttpResponse object with Excel content type
#         response = HttpResponse(
#             content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
#         )
#         response['Content-Disposition'] = f'attachment; filename="Weekly_Reports_{datetime.today().strftime("%Y-%m-%d")}.xlsx"'
#
#         # Save the output to the HttpResponse
#         output.seek(0)
#         response.write(output.getvalue())
#
#         return response


class WeeklyReport(APIView):
    def get(self, request):
        # Sample data from your database
        data = Patientopdform.objects.all().values()
        # Convert query data to DataFrame
        df = pd.DataFrame(data)
        # Check if DataFrame is empty
        if df.empty:
            return Response({"error": "No data available"}, status=400)

        df['date'] = pd.to_datetime(df['date'], format='%d-%b-%y').dt.strftime('%Y-%m-%d')
        # Create a 'Count' column
        df['Count'] = 1

        # Initialize Excel writer for output
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            # Step 1: Always create a default sheet with "No Data Available" message
            df_empty = pd.DataFrame([['No Data Available']], columns=['Message'])
            df_empty.to_excel(writer, sheet_name='No Data', index=False)

            # Step 2: Get unique values for 'week'
            weeks = df['week'].unique()
            sheet_added = False  # Flag to check if at least one valid sheet is added

            for week in weeks:
                # Filter data for the current week
                week_data = df[df['week'] == week]
                week_data = week_data.sort_values(by='day')
                # Check if there's data for the week
                if not week_data.empty:
                    actual_days = week_data['day'].unique()
                    # Create pivot table for the current week
                    pivot_table = week_data.pivot_table(
                        index=['diagnosis'],
                        columns=['day', 'villageName', 'gender'],
                        values='Count',
                        aggfunc='sum',
                        fill_value=0
                    )

                    # Add a 'Grand Total' column by summing across rows
                    pivot_table['Grand Total For M/F'] = pivot_table.sum(axis=1)

                    # Reset index
                    pivot_table.reset_index(inplace=True)

                    # Create dynamic multi-index for columns
                    week_days = week_data[['day', 'date']].drop_duplicates().sort_values(by='day')
                    day_date_map = dict(zip(week_days['day'], week_days['date']))

                    # Generate dynamic multi-index tuples
                    dynamic_columns = []
                    for (day, village, gender) in pivot_table.columns[1:-1]:
                        if day in actual_days:
                            date = day_date_map.get(day, '')
                            dynamic_columns.append((day, date, village, gender))

                    # Add 'Grand Total For M/F' at the end
                    dynamic_columns.append(('Grand Total For M/F', '', '', ''))
                    dynamic_columns = sorted(dynamic_columns, key= lambda x: pd.to_datetime(x[1]) if x[1] != '' else pd.NaT)
                    dynamic_columns = [('Diagnosis', '','','')]+ dynamic_columns

                    # Assign the multi-index to the pivot table columns

                    pivot_table.columns = pd.MultiIndex.from_tuples(dynamic_columns,
                                                                    names=['Day', 'Date', 'Village', 'Gender'])

                    # Write the pivot table to a new sheet
                    pivot_table.to_excel(writer, sheet_name=f'Week {week}', index=True)
                    sheet_added = True  # Mark that a valid sheet is added
                    # Apply borders to the entire sheet
                    workbook = writer.book
                    worksheet = workbook[f'Week {week}']

                    thin_border = Border(
                        left=Side(style='thin'),
                        right=Side(style='thin'),
                        top=Side(style='thin'),
                        bottom=Side(style='thin')
                    )

                    # Loop through all cells and apply border
                    for row in worksheet.iter_rows():
                        for cell in row:
                            cell.border = thin_border
            # Step 6: Handle case where no sheets with actual data were added
            if not sheet_added:
                df_empty.to_excel(writer, sheet_name='No Valid Data', index=False)

        # Set the pointer to the beginning of the output stream
        output.seek(0)

        # Return the Excel file as a FileResponse
        response = FileResponse(output, as_attachment=True, filename='WeeklyReport.xlsx')
        return response
