from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UserWorkDataViewSet, SkillListViewSet, UserSkillsViewSet, CertificationDataViewSet, UserProfileView

router = DefaultRouter()
router.register(r'list', UserViewSet)
router.register(r'workdata', UserWorkDataViewSet)
router.register(r'skills', UserSkillsViewSet)
router.register(r'skilllist', SkillListViewSet)
router.register(r'certifications', CertificationDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]
