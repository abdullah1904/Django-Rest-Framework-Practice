from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Person, Color


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    def validate(self, data):
        if data['username'] and User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("Username already exists")
        if data['email'] and User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("Email already exists")
        return data
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['color_name']

class PersonSerializer(serializers.ModelSerializer):
    color_id = serializers.PrimaryKeyRelatedField(queryset=Color.objects.all(), source='color',write_only=True)
    color = ColorSerializer(read_only=True)
    # color_info = serializers.SerializerMethodField()
    class Meta:
        model = Person
        fields = '__all__'
        # fields = ['id','name','age','color']
        # exclude = ['age']
        # depth = 1

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
        if data.get('age') and data['age'] < 18:
            raise serializers.ValidationError("Age must be greater than 18")
        if any(c in special_characters for c in data['name']):
            raise serializers.ValidationError("Name must not contain special characters")
        return data
    # def get_color_info(self,data):
    #     color_obj = Color.objects.get(id=data.color.id)
    #     return {"color_name": color_obj.color_name, "hex_code": "#010101"}