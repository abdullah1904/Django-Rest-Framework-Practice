from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        # fields = ['name','age']
        fields = '__all__'
        # exclude = ['age']

    # def validate_age(self,age):
    #     if age < 18:
    #         raise serializers.ValidationError("Age must be greater than 18")
    #     return age
    # def validate_name(self,name):
    #     print(name)
    #     special_characters = "!@#$%^&*()-+?_=,<>/"
    #     if any(c in special_characters for c in name):
    #         raise serializers.ValidationError("Name must not contain special characters")
    #     return name
    def validate(self, data):
        special_characters = "!@#$%^&*()-+?_=,<>/"
        if data['age'] < 18:
            raise serializers.ValidationError("Age must be greater than 18")
        if any(c in special_characters for c in data['name']):
            raise serializers.ValidationError("Name must not contain special characters")
        return data