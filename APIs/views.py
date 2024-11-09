from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Person
from .serializers import PersonSerializer, LoginSerializer, RegisterSerializer


class Register(APIView):
    # class Meta:
    #     method = ['POST']
    def post(self,request):
        data = RegisterSerializer(data = request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        return Response(data.errors)


class Login(APIView):
    def post(self,request):
        data = LoginSerializer(data=request.data)
        if data.is_valid():
            user = authenticate(username=data.data['username'], password=data.data['password'])
            if not user:
                return Response({"message": "Invalid Credentials"},status=status.HTTP_404_NOT_FOUND)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"message": "Success", "token": str(token)})
        return Response(data.errors) 

@api_view(['GET','POST','PUT'])
def index(request):
    if request.method == "GET":
        print(request.GET.get('age')) # Request Query
        return Response({"data": "hello Abdullah from GET"})
    elif request.method == 'POST':
        print(request.data) # Request Body
        return Response({"data": "hello Abdullah from POST"})
    elif request.method == 'PUT':
        return Response({"data": "hello Abdullah from PUT"})


@api_view(['POST'])
def login(request):
    data = LoginSerializer(data=request.data)
    if data.is_valid():
        return Response({"message": "Success","data": data.data})
    return Response(data.errors)


class PersonListCreateView(APIView):
    def get(self,request):
        persons = PersonSerializer(Person.objects.filter(color__isnull=False), many=True)
        return Response(persons.data)
    def post(self,request):
        data = PersonSerializer(data=request.data)
        print(data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        return Response(data.errors)


# @api_view(['GET','POST'])
# def person(request):
#     if request.method == 'GET':
#         # persons = PersonSerializer(Person.objects.all(),many=True)
#         persons = PersonSerializer(Person.objects.filter(color__isnull=False), many=True)
#         return Response(persons.data)
#     elif request.method == 'POST':
#         data = PersonSerializer(data=request.data)
#         if data.is_valid():
#             data.save()
#             return Response(data.data)
#         return Response(data.errors)


class PersonDetailView(APIView):
    def get(self, request, id):
        person = get_object_or_404(Person, id=id)
        persons = PersonSerializer(person)
        return Response(persons.data)

    def put(self, request, id):
        person = get_object_or_404(Person, id=id)
        data = PersonSerializer(person, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        return Response(data.errors)

    def patch(self, request, id):
        person = get_object_or_404(Person, id=id)
        data = PersonSerializer(person, data=request.data, partial=True)
        if data.is_valid():
            data.save()
            return Response(data.data)
        return Response(data.errors)

    def delete(self, request, id):
        person = get_object_or_404(Person, id=id)
        person.delete()
        return Response({"message": "Person Deleted"})

# @api_view(['GET','PUT','PATCH','DELETE'])
# def singlePerson(request,id):
#     person = get_object_or_404(Person,id=id)
#     if request.method == 'GET':
#         persons = PersonSerializer(person)
#         return Response(persons.data)
#     elif request.method == 'PUT':
#         data = PersonSerializer(person,data=request.data)
#         if data.is_valid():
#             data.save()
#             return Response(data.data)
#         return Response(data.errors)
#     elif request.method == 'PATCH':
#         data = PersonSerializer(person,data=request.data,partial=True)
#         if data.is_valid():
#             data.save()
#             return Response(data.data)
#         return Response(data.errors)
#     elif request.method == 'DELETE':
#         person.delete()
#         return Response({"message": "Person Deleted"})

class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def list(self, request):
        try:
            search = request.GET.get('search')
            page = request.GET.get('page',1)
            page_size = 1
            queryset = self.queryset
            if(search):
                queryset = queryset.filter(name__startswith=search)
            paginator = Paginator(queryset,page_size)
            data = PersonSerializer(paginator.page(page),many=True)
            return Response({'message': 'OK','data': data.data})
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    # def destroy(self, request, *args, **kwargs):
    #     response = super().destroy(request, *args, **kwargs)
    #     if response.status_code == status.HTTP_204_NO_CONTENT:
    #         return Response({'message': 'Person deleted successfully'}, status=status.HTTP_200_OK)
    #     return response