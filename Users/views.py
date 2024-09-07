from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes, authentication_classes
from .models import UserProfile, UserWorkData, UserSkills, CertificationData
from Users.auxiliary_models import skillList
from .serializers import UserSerializer, UserWorkDataSerializer, UserSkillsSerializer, CertificationDataSerializer, SkillListSerializer
from .serializers import UserProfileSerializer
from rest_framework import generics, permissions


@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

class UserWorkDataViewSet(viewsets.ModelViewSet):
    queryset = UserWorkData.objects.all()
    serializer_class = UserWorkDataSerializer
    permission_classes = [IsAuthenticated]

class SkillListViewSet(viewsets.ModelViewSet):
    queryset = skillList.objects.all()
    serializer_class = SkillListSerializer
    permission_classes = [IsAuthenticated]

class UserSkillsViewSet(viewsets.ModelViewSet):
    queryset = UserSkills.objects.all()
    serializer_class = UserSkillsSerializer
    permission_classes = [IsAuthenticated]

class CertificationDataViewSet(viewsets.ModelViewSet):
    queryset = CertificationData.objects.all()
    serializer_class = CertificationDataSerializer
    permission_classes = [IsAuthenticated]

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
