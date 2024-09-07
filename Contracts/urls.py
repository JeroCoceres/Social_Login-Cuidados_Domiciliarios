from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContractViewSet, SkillRequiredViewSet, ComfortOfferedViewSet, ChecklistViewSet

router = DefaultRouter()
router.register(r'list', ContractViewSet)
router.register(r'skill-required', SkillRequiredViewSet)
router.register(r'comfort-offered', ComfortOfferedViewSet)
router.register(r'checklists', ChecklistViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
