from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status, generics, mixins, viewsets
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authtoken.models import Token


# Create your views here.


class TodoView(APIView):
    def post(self, request):
        a = TodoSerializer(data=request.data)
        if a.is_valid():
            a.save()
            return Response(a.data)

    def get(self, request):
        a = TodoModel.objects.all()
        b = TodoSerializer(a, many=True)
        return Response(b.data)


# class StudentView(APIView):
#     def post(self, request):
#         a = StudentSerializer(data=request.data)
#         if a.is_valid():
#             a.save()
#             return Response({"Alert": "Student Details Added"})
#
#     def get(self, request):
#         a = StudentModel.objects.all()
#         b = StudentSerializer(a, many=True)
#         return Response(b.data)


class TodoDetailView(APIView):
    def get(self, request, **kwargs):
        a = kwargs.get("id")
        b = TodoModel.objects.get(id=a)
        c = TodoSerializer(b)
        return Response(c.data)

    def put(self, request, **kwargs):
        a = kwargs.get("id")
        b = TodoModel.objects.get(id=a)
        c = TodoSerializer(instance=b, data=request.data)
        if c.is_valid():
            c.save()
            return Response(c.data)

    def delete(self, request, **kwargs):
        a = kwargs.get("id")
        b = TodoModel.objects.get(id=a)
        b.delete()
        return Response({'msg': 'Deleted'})


class RegistrationView(APIView):
    def post(self, request):
        a = RegistrationSerializer(data=request.data)
        if a.is_valid():
            a.save()
            return Response({'msg': 'Registration success'}, status=status.HTTP_201_CREATED)
        else:
            return Response(a.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        a = User.objects.all()
        b = RegistrationSerializer(a, many=True)
        return Response(b.data)


class LoginView(APIView):
    def post(self, request):
        a = LoginSerializer(data=request.data)
        if a.is_valid():
            nm = a.validated_data.get("username")
            ps = a.validated_data.get("password")
            b = authenticate(username=nm, password=ps)
            if b:
                login(request, b)
                return Response({'msg': 'Login success'})
            else:
                return Response({'msg': 'Login failed'})


class PersonView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    serializer_class = PersonSerializer
    queryset = PersonModel.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PersonDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin):
    serializer_class = PersonSerializer
    queryset = PersonModel.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# class EmployeeView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
#     serializer_class = EmployeeSerializer
#     queryset = EmployeeModel.objects.all()
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


# class EmployeeDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
#                          mixins.DestroyModelMixin):
#     serializer_class = EmployeeSerializer
#     queryset = EmployeeModel.objects.all()
#     lookup_field = 'id'
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


class MovieView(viewsets.ViewSet):
    serializer_class = MovieSerializer
    model = MovieModel

    def create(self, request):
        a = self.serializer_class(data=request.data)
        if a.is_valid():
            a.save()
            return Response(a.data, status=status.HTTP_201_CREATED)
        else:
            return Response(a.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        a = self.model.objects.all()
        b = self.serializer_class(a, many=True)
        return Response(b.data, status=status.HTTP_200_OK)

    def update(self, request, **kwargs):
        a = kwargs.get("pk")
        b = self.model.objects.get(id=a)
        c = self.serializer_class(data=request.data, instance=b)
        if c.is_valid():
            c.save()
            return Response(c.data, status=status.HTTP_200_OK)
        else:
            return Response(c.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, **kwargs):
        a = kwargs.get("pk")
        b = self.model.objects.get(id=a)
        c = self.serializer_class(b)
        return Response(c.data, status=status.HTTP_200_OK)

    def destroy(self, request, **kwargs):
        a = kwargs.get("pk")
        b = self.model.objects.get(id=a)
        b.delete()
        return Response({'msg': 'deleted'}, status=status.HTTP_200_OK)


# class BookView(viewsets.ViewSet):
#     serializer_class = BookSerializer
#     model = BookModel
#
#     def create(self, request):
#         a = self.serializer_class(data=request.data)
#         if a.is_valid():
#             a.save()
#             return Response(a.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(a.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def list(self, request):
#         a = self.model.objects.all()
#         b = self.serializer_class(a, many=True)
#         return Response(b.data, status=status.HTTP_200_OK)
#
#     def retrieve(self, request, **kwargs):
#         a = kwargs.get("pk")
#         b = self.model.objects.get(id=a)
#         c = self.serializer_class(b)
#         return Response(c.data, status=status.HTTP_200_OK)
#
#     def update(self, request, **kwargs):
#         a = kwargs.get("pk")
#         b = self.model.objects.get(id=a)
#         c = self.serializer_class(data=request.data, instance=b)
#         if c.is_valid():
#             c.save()
#             return Response(c.data, status=status.HTTP_200_OK)
#         else:
#             return Response(c.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def destroy(self, request, **kwargs):
#         a = kwargs.get("pk")
#         b = self.model.objects.get(id=a)
#         b.delete()
#         return Response({'msg': 'deleted'}, status=status.HTTP_200_OK)


class CompanyView(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = CompanyModel.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]


class UserView(APIView):
    def post(self, request):
        a = UserSerializer(data=request.data)
        if a.is_valid():
            a.save()
            b = User.objects.get(username=a.data['username'], email=a.data['email'])
            token_obj, _ = Token.objects.get_or_create(user=b)
            return Response({'msg': 'Registration success', 'token': str(token_obj)}, status=status.HTTP_201_CREATED)
        else:
            return Response(a.errors, status=status.HTTP_400_BAD_REQUEST)
