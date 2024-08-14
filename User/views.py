from django.db.models import Q

import jwt
import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from django.conf import settings
from User.models import User
from User.serializers import UserSerializer, LoginSerializer

# Create your views here.
class UserAPI(ModelViewSet):
          queryset = User.objects.all()
          serializer_class = UserSerializer

          def list(self, request, *args, **kwargs):
                    try:
                              user = User.objects.all()
                              serializer = self.get_serializer(user, many=True)
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'All user',
                                        'all_user': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_message = 'An error occurred while fetching user: {}'.format(str(e))
                    error_response = {
                              'status': 'error',
                              'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                              'message': error_message
                    }
                    return Response(error_response)

          def retrieve(self, request, *args, **kwargs):
                    try:
                              instance = self.get_object()
                              serializer = self.get_serializer(instance)
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'User fetched successfully',
                                        'user_details': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_message = 'An error occurred while fetching user: {}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                                        'message': error_message
                              }
                    return Response(error_response)

          def create(self, request, *args, **kwargs):
                    try:
                              serializer = self.serializer_class(data=request.data)
                              serializer.is_valid(raise_exception=True)
                              serializer.save()

                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_201_CREATED,
                                        'message': 'User added successfully',
                                        'new_user': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_message = 'Failed to add user: {}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_400_BAD_REQUEST,
                                        'message': error_message
                              }
                              return Response(error_response)

          def update(self, request, *args, **kwargs):
                    try:
                              instance = self.get_object()
                              serializer = self.get_serializer(instance, data=request.data)
                              serializer.is_valid(raise_exception=True)
                              serializer.save()

                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'User updated successfully',
                                        'updated_user': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_message = 'Failed to update user:{}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_400_BAD_REQUEST,
                                        'message': error_message
                              }
                              return Response(error_response)

          def partial_update(self, request, *args, **kwargs):
                    try:
                              instance = self.get_object()
                              serializer = self.get_serializer(instance, data=request.data, partial=True)
                              serializer.is_valid(raise_exception=True)
                              serializer.save()

                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'User updated successfully',
                                        'updated_user': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_message = 'Failed to partially update user:{}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_400_BAD_REQUEST,
                                        'message': error_message
                              }
                              return Response(error_response)

          def destroy(self, request, *args, **kwargs):
                    try:
                              instance = self.get_object()
                              instance.delete()

                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_204_NO_CONTENT,
                                        'message': 'User deleted successfully',
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_message = 'Failed to delete user:{}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_400_BAD_REQUEST,
                                        'message': error_message
                              }
                    return Response(error_response)

class UserLoginAPI(APIView):
          def post(self, request, *args, **kwargs):
                    serializer = LoginSerializer(data=request.data)
                    if serializer.is_valid():
                              username_or_mobileno = serializer.validated_data.get('username')
                              password = serializer.validated_data.get('password')

                              try:
                                        # Check if the user exists using username or mobileno
                                        user = User.objects.filter(
                                                  Q(username=username_or_mobileno) |
                                                  Q(mobileno=username_or_mobileno)
                                        ).first()

                                        if user:
                                                  # Compare the passwords directly
                                                  if password == user.password:
                                                            # Generate JWT token
                                                            payload = {
                                                                      'uid': user.uid,
                                                                      'exp': datetime.datetime.utcnow() + datetime.timedelta(
                                                                                days=1),
                                                                      'iat': datetime.datetime.utcnow()
                                                            }
                                                            token = jwt.encode(payload, settings.SECRET_KEY,
                                                                               algorithm='HS256')

                                                            return Response(
                                                                      {
                                                                                'status': 'success',
                                                                                'message': 'Login successful',
                                                                                'username': user.username,
                                                                                'role': user.role,
                                                                                'token': token
                                                                      },
                                                                      status=status.HTTP_200_OK,
                                                                      headers={'Authorization': f'Bearer {token}'}
                                                            )
                                                  else:
                                                            return Response(
                                                                      {'status': 'error',
                                                                       'message': 'Invalid password'},
                                                                      status=status.HTTP_401_UNAUTHORIZED
                                                            )
                                        else:
                                                  return Response(
                                                            {'status': 'error', 'message': 'User not found'},
                                                            status=status.HTTP_404_NOT_FOUND
                                                  )

                              except Exception as e:
                                        return Response(
                                                  {'error': str(e)},
                                                  status=status.HTTP_500_INTERNAL_SERVER_ERROR
                                        )

                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
