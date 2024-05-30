from django.urls import path
from rest_framework import routers

from app_publications.views import (
    SphereViewSet,
    ReviewerViewSet,
    ReferencesViewSet,
    PublicationsViewSet, PapersViewSet,
    FeedbacksViewSet,
    get_article,
    RequirementViewSet, FAQViewSet,
    contact_view,
)

router = routers.DefaultRouter()

router.register('spheres', SphereViewSet, basename='spheres')
router.register('reviewers', ReviewerViewSet, basename='reviewers')
router.register('references', ReferencesViewSet, basename='references')
router.register('publications', PublicationsViewSet, basename='publications')
router.register('papers', PapersViewSet, basename='papers')
router.register('feedbacks', FeedbacksViewSet, basename='feedbacks')
router.register('requirements', RequirementViewSet, basename='requirements')
router.register('faq', FAQViewSet, basename='faq')

urlpatterns = router.urls

urlpatterns += [
    path('article-detail/<int:article_id>/', get_article, name="article-detail"),
    path('contact', contact_view, name='contact')
]