from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class EmployeeRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'city', 'phone_number', 'state', 'address', 'department', 'project_name', 'date_of_joined', 'designation', 'is_still_in_company')

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            city=validated_data['city'],
            phone_number=validated_data['phone_number'],
            state=validated_data['state'],
            address=validated_data['address'],
            department=validated_data['department'],
            project_name=validated_data['project_name'],
            date_of_joined=validated_data['date_of_joined'],
            is_still_in_company=validated_data['is_still_in_company'],
            designation = validated_data['designation']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100, write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise serializers.ValidationError('Please provide both email and password.')

        return data