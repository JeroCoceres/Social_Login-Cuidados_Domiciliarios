from rest_framework import serializers
from .models import UserProfile, UserWorkData, UserSkills, CertificationData
from Users.auxiliary_models import skillList

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Añade el campo password como write-only

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'password', 'userIsWorker', 'userMembership', 'userGender', 'userBirthDate', 'userLocation', 'userDescription', 'userProvince', 'userCity', 'userPostalCode']

    def create(self, validated_data):
        password = validated_data.pop('password')  # Extrae la contraseña del validated_data
        user_instance = UserProfile.objects.create(**validated_data)
        user_instance.set_password(password)  # Hashea la contraseña usando set_password
        user_instance.save()
        return user_instance

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['userIsWorker', 'userMembership', 'userGender', 'userBirthDate', 'userLocation', 'userDescription', 'userProvince', 'userCity', 'userPostalCode']

class UserWorkDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWorkData
        fields = ['userID', 'workerID', 'MinPayment', 'isStudying', 'userProfession']

class SkillListSerializer(serializers.ModelSerializer):
    class Meta:
        model = skillList
        fields = ['skillID', 'skillName']

class UserSkillsSerializer(serializers.ModelSerializer):
    userID = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(), many=True)
    skillID = serializers.PrimaryKeyRelatedField(queryset=skillList.objects.all())

    class Meta:
        model = UserSkills
        fields = ['userID', 'skillID', 'description', 'hasExperience', 'yearsOfExperience', 'isVerified']

class CertificationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificationData
        fields = ['skillID', 'certificateID', 'institution', 'certificateDate', 'file']
