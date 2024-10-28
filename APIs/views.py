from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Person
from .serializers import PersonSerializer, LoginSerializer
from django.shortcuts import get_object_or_404

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